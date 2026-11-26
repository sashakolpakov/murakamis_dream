# The actual microscopic derivative is a finite sum of signed crossing insertions

Research deduction, 6 November 2026.

The fixed-root meridian derivative of the whole reduced knot scalar
has an explicit presentation by the original crossing products.
There is one differentiated crossing family per crossing of a fixed
braid. Each derivative is a diagonal index insertion plus a sum of
products with one factor deleted. These are whole polynomial
identities, including at zeros of the original factors.

The source-frame commutators cancel under the original closure.
The differentiated crossing insertions do not disappear for that
reason. After canonical ordinary-color subtraction, the estimate
still needed is a signed contraction bound stated in Section 5.
It would imply the microscopic observation estimate without
dividing by the complete value. No such bound for arbitrary knots
is asserted here.

## 1. Fixed-root conventions and the complete original contraction

Fix a braid on \(m\) strands whose closure is a zero-framed knot.
The word and its length \(\ell\) are fixed before the level.
Use
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad n=N-1,\quad
 M=e^{\zeta/(2N)},\quad Y=M^2=e^{\zeta/N},\quad
 \beta=\frac{\zeta}{2\pi i},\quad x=-\frac Mq,\quad
 \lambda_N=\frac n{2N}.
 \tag{1}
\]
In particular \(Q^\beta=e^{\zeta/N}\) denotes this specified
entire function, not a choice of logarithm made after evaluation.
The quantum parameter stays fixed. The moving-\(q\), fixed-integral-
color normal in the
[finite-jet source connection](actual_tensor_source_finite_jet_connection.md)
is a different derivative.

Take the literal balanced crossing formulas of
[the common-Verma source](common_verma_two_wall_source.md), Section 3,
and [the crossing comparison](actual_crossing_q_normal_meridian_ratio.md),
Sections 1–2. Write \({a\brack k}_Q\) for their polynomial Gaussian.
The positive and negative zero-framing-normalized coefficients are
\[
\begin{split}
 C_+(i,j,k;\zeta)
 &=A_+(i,j,k;\zeta)
       \prod_{h=i-k+1}^{i}(1-Q^{\beta-h}),\\
 A_+
 &=(-1)^k x^{\,n-i-j-k}
     Q^{ij+(i-j)k-k(k+1)/2}{j+k\brack k}_Q,\\
 C_-(i,j,k;\zeta)
 &=A_-(i,j,k;\zeta)
       \prod_{h=j-k+1}^{j}(1-Q^{\beta-h}),\\
 A_-
 &=x^{\,i+j-k-n}Q^{-ij}{i+k\brack k}_Q .
\end{split}
\tag{2}
\]
The positive route is \((i,j)\mapsto(j+k,i-k)\), with
\(0\le k\le\min(i,n-j)\). The negative route is
\((i,j)\mapsto(j-k,i+k)\), with
\(0\le k\le\min(j,n-i)\). Every index is physical:
\(0\le i,j<N\). In particular every factor label \(h\) in (2)
lies in \(\{1,\ldots,N-1\}\).

The factors \(x^{\pm n}\) in (2) implement the original
zero-framing correction. They follow by cancelling each full
Cartan scalar against its matching twist; no full crossing
scalar is being discarded. Each of the \(m-1\) original
closed pivots is still
\[
                 K^{1-N}v_j=x^{-n}Q^{nj}v_j .
 \tag{3}
\]
Use the original reduced highest-weight cut on the remaining
strand. Balanced basis changes in (2) depend on \(q\), not \(M\),
and preserve this scalar and the partial trace. Thus the exact
source of
[the ADO pointing](kashaev_ado_pointing.md), Sections 1–2, is
\[
 f_N(\zeta):=F_N(e^{\zeta/N})
 =x^{-n(m-1)}
   \sum_{\omega\in\Omega_N}
       Q^{\,n\sum_{\text{closed heads}}j(\omega)}
       \prod_{v=1}^{\ell}C_{\epsilon_v}
                 (i_v(\omega),j_v(\omega),k_v(\omega);\zeta).
 \tag{4}
\]
Here \(\Omega_N\) is the original finite set of compatible
physical paths, including the original first input and output
and the closing equalities. It is independent of \(\zeta\).
The signs and phases in this sum remain literal. Formula (4)
holds at both level parities and for arbitrary crossing signs;
the empty one-strand word gives \(f_N=1\).

## 2. The differentiated local families are zero-safe

For either sign let \(H_\epsilon\) be the interval of factor
labels in (2), and put
\[
 a_+=\frac{n-i-j-k}{2N},\qquad
 a_-=\frac{i+j-k-n}{2N},\qquad
 E_h=Q^{\beta-h}.
 \tag{5}
\]
Because \(\partial_\zeta E_h=E_h/N\) and
\(\partial_\zeta A_\epsilon=a_\epsilon A_\epsilon\),
the actual differentiated coupon is exactly
\[
 \dot C_\epsilon
 =a_\epsilon C_\epsilon
   -\frac{A_\epsilon}{N}
       \sum_{h\in H_\epsilon}E_h
          \prod_{\substack{t\in H_\epsilon\\t\ne h}}(1-E_t).
 \tag{6}
\]
For \(k=0\) the sum is empty. Formula (6) is an identity of
entire microscopic functions. It never divides by a vanishing
Pochhammer factor. Equivalently, using \(-E_h=(1-E_h)-1\),
one may replace \(a_\epsilon\) by \(a_\epsilon+k/N\) and
replace \(E_h\) in the sum by \(1\).
Thus a fixed crossing has one diagonal family and one
one-factor-deleted family. The deleted-factor label is summed
inside that family; the number of families does not grow
with \(N\).

Let \(\mathcal D_{v,N}(\zeta)\) be precisely (4), with crossing
\(v\) replaced by (6), all other crossings and every pivot
unchanged. Differentiating the fixed finite sum gives
\[
 \boxed{\displaystyle
       f_N'(\zeta)
       =\sum_{v=1}^{\ell}\mathcal D_{v,N}(\zeta)
                         -\lambda_N(m-1)f_N(\zeta).}
 \tag{7}
\]
The last term is the derivative of the \(m-1\) pivotal
monomials in (3). It must not be counted a second time
among the crossing factors.

For comparison, a true but insufficient coefficient estimate
can be proved without an asymptotic source theorem. Fix \(r<1\)
and \(|\beta|\le r\). For \(1\le h<N\),
\[
 |1-Q^{\beta-h}|
 \ge \frac{4e^{-\pi r/N}(1-r)}{N}\min(h,N-h).
 \tag{8}
\]
Indeed \(|\sin(a+ib)|\ge|\sin a|\), and the real sine argument
lies between the two adjacent root positions with distance at
least \((1-r)\min(h,N-h)\) from an endpoint. Also
\(|E_h|\le e^{2\pi r/N}\) and \(|a_\epsilon|\le1/2\).
Consequently
\[
       |\dot C_\epsilon|\le C_r(1+\log N)|C_\epsilon|
                    \qquad(|\beta|\le r).
 \tag{9}
\]
The Gaussian factors are nonzero on their physical support,
so the displayed comparison is legitimate on this small disk.
Equation (6), rather than (9), is the definition on larger disks
or at zeros. The pathwise estimate (9) gives a total-variation
bound after closure, not a bound by the modulus of the signed
sum in (4).

## 3. Frame currents cancel; crossing insertions remain

The global horizontal braid frame in
[the exact open transport](actual_open_meridian_horizontal_source_transport.md),
Section 3, uses
\(G(M)=\bigotimes_{j=0}^{m-1}M^{-jJ_j}\).
The first cut has \(j=0\); every closed pivot is diagonal and
commutes with the frame. Adjacent frame changes cancel in the
word before closure. Differentiating gives commutators, whose
original partial quantum traces vanish because the pivotal
matrices commute with the frame generator. Equivalently one
can conjugate the pivotal matrices and all coupons together
into the Fourier frame. On its second wire the microscopic
generator is
\[
       (\partial_\zeta W)W^{-1}
                 =\frac{\ell_0}{2N}VJV^{-1},
           \qquad \|(\partial_\zeta W)W^{-1}\|
                    \le\frac{\ell_0}{2}
 \tag{10}
\]
at the principal root, where \(\ell_0\) is the fixed strand
position of that cut and \(V/\sqrt N\) is unitary. This bound
is not a bound on the knot word. The trace cancellation is
exact on all current tensors and makes (7) independent of
this source-preserving choice of frame.

On a regular proper-array chart, write
\(\mathcal J=\partial_\zeta I/I\) and
\(R_i=S_iI/I\) for the actual source and its internal shift
ratios. Then
\[
 \partial_\zeta R_i=R_i(S_i\mathcal J-\mathcal J),\qquad
 [\,\partial_\zeta+\mathcal J,\ R_iS_i-1\,]=0 .
 \tag{11}
\]
This is the infinitesimal source/current identity. Its global
meaning is the differentiated, zero-extended whole-product
identity (6), with all original finite boundaries retained.
It does not say that \(\mathcal J\) is scalar modulo currents.
For example, multiplication of an ordinary finite difference
by \(\mathcal J\) leaves the exact summation-by-parts term
\[
 \sum_{\mathbf s}\mathcal J(\mathbf s)(S_i-1)H(\mathbf s)
 =\sum_{\mathbf s}
       [\mathcal J(\mathbf s-e_i)-\mathcal J(\mathbf s)]
                                      H(\mathbf s),
 \tag{12}
\]
when written on a regular chart and then interpreted by
whole products. Dropping this term is not justified by
the frame cancellation. The finite-jet moving-period connection
does not identify this fixed-\(q\) insertion with a scalar either.

## 4. Exact regularization, balanced Weyl identity, and the first missing jet

Keep the canonical functions of
[the regularized period](regularized_kashaev_period.md):
\[
 F_N(Y)=S_N(Y)R_N(Y)+P_N(Y),\qquad
 S_N(Y)=\sum_{j=0}^{N-1}Y^j,\qquad
 p_N(\zeta)=P_N(e^{\zeta/N}).
 \tag{13}
\]
The letter \(p_N\) in this note denotes this microscopic
polynomial evaluation, not the polar quotient \(P_N/S_N\).
The ordinary-color theorem gives
\[
 |[Y^j]P_N|\le2D_N,\quad 0\le j\le N-2,\qquad
 D_N\le(N/2)^{m-1}.
 \tag{14}
\]
Define the unnormalized balanced regular function
\[
 W_N(\zeta)=e^{\lambda_N\zeta}R_N(e^{\zeta/N}),\qquad
 H_N(\zeta)=\frac{\sinh(\zeta/2)}
                         {N\sinh(\zeta/(2N))}.
 \tag{15}
\]
The removable values are understood. The exact identity is
\(f_N=NH_NW_N+p_N\), with the original \(N\) and original
full-state monomial retained.

Fix \(0<r_0<2\pi\). On its closed disk, \(H_N\) is nonzero
and \(H_N\), \(H_N^{-1}\), and
\(h_N=H_N'/H_N\) are uniformly bounded for all sufficiently
large levels. Put
\[
 \begin{split}
 \mathcal I_N(\zeta)
   &=\sum_{v=1}^{\ell}\mathcal D_{v,N}(\zeta)
        -[\lambda_N(m-1)+h_N(\zeta)]f_N(\zeta),\\
 \mathcal E_N(\zeta)&=p_N'(\zeta)-h_N(\zeta)p_N(\zeta).
 \end{split}
 \tag{16}
\]
Then the whole regularized derivative is exactly
\[
                  \boxed{NH_NW_N'=\mathcal I_N-\mathcal E_N.}
 \tag{17}
\]
In particular the correction from ordinary colors is subtracted,
not discarded. For every fixed derivative order, (14) bounds
the corresponding derivative of \(p_N\) by \(C_{r_0}ND_N\).
Thus \(\mathcal E_N\) has polynomial size on this disk.

The actual Weyl theorem gives \(f_N(-\zeta)=f_N(\zeta)\);
\(H_N\) is also even. Hence
\[
 H_N(\zeta)[W_N(\zeta)-W_N(-\zeta)]
                 =\frac{p_N(-\zeta)-p_N(\zeta)}{N}.
 \tag{18}
\]
This is the balanced symmetry, not evenness of the uncentered
regular Laurent coefficient. In particular (7) and (17) give
the actual signed insertion identities
\[
 \sum_v\mathcal D_{v,N}(0)=\lambda_N(m-1)K_N,\qquad
 W_N'(0)=-\frac{P_N'(1)}{N^2},\qquad
 W_N(0)=\frac{K_N-P_N(1)}{N}.
 \tag{19}
\]
These require no nonzero assumption on \(K_N\). All fixed odd
balanced jets are polynomially bounded, as proved in
[the unnormalized profile comparison](scaled_meridian_regular_profile.md),
Section 4.1. The first unspecified balanced jet is even:
\[
 N W_N''(0)
   =f_N''(0)-p_N''(0)
       -\frac{N^2-1}{12N^2}[K_N-P_N(1)] .
 \tag{20}
\]
Here \(f_N''(0)\) is the literal sum with two differentiated
crossings, or one twice-differentiated crossing, and the
corresponding pivot derivatives. Its factors remain zero-safe
by differentiating (6). Weyl symmetry does not bound this
signed second-order insertion by \(K_N\).

## 5. The concrete signed estimate sufficient for observation

The remaining requirement can be formulated using only the
fixed finite list of actual families in (6), their original
closed contractions, and the known scalar subtractions (16).
Suppose on one fixed disk \(0<r_0<2\pi\) there are numbers
\[
 a_N\ge0,\quad a_N=o(N),\qquad B_N\ge1,\quad
                   \log B_N=o(N),
\]
such that the **signed contracted insertion** obeys
\[
       |\mathcal I_N(\zeta)|
           \le a_N|f_N(\zeta)-p_N(\zeta)|+B_N
                    \qquad(|\zeta|\le r_0).
 \tag{21}
\]
The original phases must be summed before applying this
inequality. It is enough, but not necessary, to obtain it
by reducing these particular insertions by exact finite
currents with subexponentially controlled remaining
contractions. Neither (9) nor (11) establishes (21).

**Proposition.** Estimate (21) implies, for every fixed \(R>0\),
\[
 \sup_{|\zeta|\le R}|R_N(e^{\zeta/N})|
                   \le e^{o(N)}(1+|K_N|).
 \tag{22}
\]
It does so without division by \(K_N\), including levels at
which that value vanishes.

Indeed (17), the uniform bounds for \(H_N^{\pm1}\), and
(14) give
\[
             |W_N'|\le a_N|W_N|+b_N,\qquad
                              \log(1+b_N)=o(N).
 \tag{23}
\]
Integrate along each straight segment from zero inside the
disk. The resulting elementary bound is
\[
 \sup_{|\zeta|\le r_0}|W_N(\zeta)|
       \le [\,|W_N(0)|+r_0b_N\,]e^{r_0a_N}.
 \tag{24}
\]
Equations (14), (19) give the asserted small-disk estimate.
The bounded factor \(e^{-\lambda_N\zeta}\) returns to \(R_N\).
The actual source already has a fixed linear Laurent-degree
window and a coarse exponential bound. Therefore
[fixed-radius transfer](research_subexponential_variation_meridian_observation.md),
Lemma 1, extends this estimate to every fixed \(R\), with
only \(\exp[O(N/\log N)]\) additional cost.

Thus the exact current calculation does identify a concrete
remaining source estimate: (21) for the original differentiated
crossing families. It has not proved that estimate, a scalar
differential closure of those families, or a complete-value
lower bound. It does prove the finite source presentation
(7), its frame independence, the ordinary-color cancellation
(17), and the complete first-jet identities (19).
