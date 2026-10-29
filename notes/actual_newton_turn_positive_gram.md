# A positive Newton metric for genuine original tangle turns

29 October 2026. The genuine quarter-turn of ANY original two-head Hopf
box is a unitary reversal in an explicit full-dimensional Newton
packet. Both original marked closures have dual norm ONE. Signed
crossings have an explicit adjoint in this same metric, so a specified
class of reflected rational/arborescent circuits is an exact positive
norm of its coherent half-network. This is not positivity for an
arbitrary fully augmented diagram, and no general sharp energy or new
volume-equality class is inferred.

## 1. Actual operators and the normalized Newton packet

Keep the full original algebra and source of
[the pair commutant theorem](actual_pair_casimir_commutant_and_rotated_trace.md)
and [the circle sewing theorem](general_augmented_graph_source_extension.md):

\[
 \mathcal H_N=\mathbb C[z]/P_N,\quad P_N=2T_N(z/2)+2,\quad
 c_j=q^{2j+1}+q^{-2j-1},\quad d=N-1,\quad Q=q^2 .
\]

All \(c_j\) are real, with \(c_{d-j}=c_j\). Let
\[
 F_r=(Q;Q)_r,\quad s_r=|F_r|,\quad
 B_r(z)=\prod_{j=0}^{r-1}(c_j-z),\qquad
 \widehat B_r=B_r/s_r^2,\quad 0\leq r\leq d .             \tag{1}
\]
Here \(s_0=1,\ s_d=N,\ s_rs_{d-r}=N\). The basis (1) is a
CASIMIR Newton basis, distinct from earlier normalized homogeneous
interval/length blocks. In particular its zero slot is exactly \(1\).

The original marked functional and genuine UNSCALED turn are
\[
 \phi(f)=(-1)^dN^2[z^d](f\bmod P_N),\qquad
 (\mathscr R f)_{(a,b);(c,e)}
       =x^{a-e}f(\Omega)_{(d-a,c);(b,d-e)}.              \tag{2}
\]
The turn preserves the full Hopf algebra, satisfies \(\mathscr R^2=I\),
and includes both actual cup/cap factors; it is not the scaled \(Z\)
and is not multiplicative.

## 2. Full physical proof of the Newton turn identity

For the physical degree block \(W_t\), \(0\leq t\leq d\), the
Casimir is an irreducible tridiagonal matrix with characteristic AND
minimal polynomial
\[
 \prod_{j=0}^t(z-c_j).
 \tag{3}
\]
The characteristic formula follows by the explicit generic
highest-weight/descendant triangular decomposition before regular
specialization, as in the pair commutant proof. The root offdiagonal
entries are nonzero; hence a boundary vector is cyclic, and (3) is
the minimal polynomial even when some \(c_j\) coincide. Thus \(B_r\)
annihilates \(W_t\) whenever \(t<r\), INCLUDING its Jordan normals.

Every degree block of \(B_r(\Omega)\) has first-color bandwidth at
most \(r\). In (2) the difference of its first colors is
\((d-a)-b=d-(a+b)\). Therefore \(\mathscr R B_r\) annihilates
every physical degree \(t<d-r\). Applying (3) at \(t=d-r-1\)
shows that its representing polynomial is divisible by \(B_{d-r}\);
when \(r=d\) this assertion is vacuous.

For the reverse degree bound, use the middle block \(A=\Omega|_{W_d}\).
Its turned first column is
\[
 (\mathscr R B_r(A))_{a0}
       =x^{a-d}(B_r(\Omega))_{(d-a,0);(d-a,0)} .
\]
This vanishes for \(a>d-r\), by (3). A polynomial of degree \(k<N\)
in the irreducible tridiagonal \(A\), applied to \(e_0\), has nonzero
component \(k\) from its unique outermost path. Hence
\(\deg(\mathscr R B_r)\leq d-r\). It follows that
\(\mathscr R B_r=C_rB_{d-r}\).

The scalar comes from ONE literal physical entry:
\[
 (\mathscr R B_r)_{(0,d-r);(d-r,0)}
       =(B_r)_{(d,d-r);(d-r,d)}=s_r^2 .
\]
For clarity, in the latter high-degree block the unique \(r\)-step
path increasing the first color has entries
\[
 Q^{j-r}(1-Q^{r-j})(1-Q^{j+1}),\quad0\leq j<r .
\]
Multiplying and including the leading coefficient \((-1)^r\) gives
\((-1)^rQ^{-r(r+1)/2}F_r^2=s_r^2\).
Similarly the unique decreasing path for \(B_{d-r}\) in the
LOW block of degree \(d-r\) gives \(s_{d-r}^2\).
All turn monomials in this chosen entry equal one. Consequently
\[
 \boxed{\quad
 \mathscr R B_r=\frac{s_r^2}{s_{d-r}^2}B_{d-r},
 \qquad \mathscr R\widehat B_r=\widehat B_{d-r}.
 \quad}                                                   \tag{4}
\]
This proof works for all \(N\geq2\), all \(r\), and all repeated
Casimir nodes. It uses physical matrix support and full minimal
polynomials, not an equality only on distinct eigenvalues.

## 3. Positive Gram, all ports open, and the exact original source

The full Frobenius pairing in this basis is especially simple:
\[
 \phi(\widehat B_i\widehat B_j)=\delta_{i+j,d}.             \tag{5}
\]
For \(i+j<d\) use degree. For \(i+j=d\) use its leading coefficient
and \(s_is_j=N\). If \(i+j\geq N\), the product is divisible by
\(P_N\): indeed \(B_N/B_j=B_{N-j}\), since \(c_{d-k}=c_k\),
and \(B_i\) is divisible by \(B_{N-j}\). This is polynomial
divisibility with FULL multiplicities, so (5) retains all normals.

Write \(f=\sum_r\alpha_r\widehat B_r\) and let
\(f^\sharp(z)=\overline{f(\bar z)}\). All basis polynomials in (1)
have real coefficients. Equations (4)--(5) prove the positive
definite all-input identity
\[
 \boxed{\quad
 \langle f,g\rangle_{\rm Newt}
       :=\phi(f^\sharp\mathscr Rg)
       =\sum_{r=0}^d\overline{\alpha_r}\beta_r,\qquad
 \|\mathscr R f\|_{\rm Newt}=\|f\|_{\rm Newt}.
 \quad}                                                   \tag{6}
\]
The metric is prescribed independently of any knot or exterior.
It is not the canonical unweighted Hermite-channel Gram whose energy
was excessive in a previous figure-eight test, nor the terminal \(T^*T\)
metric. Its change of frame can have exponential condition number.

The exact packet transform is
\[
 \alpha_r=(-1)^rs_r^2 f[c_0,\ldots,c_r],                 \tag{7}
\]
with confluent divided differences at repeated nodes. Thus it is
explicit and invertible on the COMPLETE algebra and retains every
first derivative, including even/composite levels.

Equivalently let \(B\) be the ACTUAL complete source-Hom bidiagonal
Casimir
\[
 Be_j=c_je_j+b_je_{j-1},\qquad
 b_j=Q^j+Q^{-j}-2=-|1-Q^j|^2 .
\]
Its cyclic column obeys \(f(B)e_d=(\alpha_d,\ldots,\alpha_0)^T\).
This follows either from its confluent divided-difference formula or
from \(\widehat B_r(B)e_d=e_{d-r}\).
Consequently
\[
 \phi(f\,\mathscr Rg)=(f(B)e_d)^T(g(B)e_d),\qquad
 f(B)e_d\mapsto P_{\rm rev}f(B)e_d
 \text{ under }\mathscr R .                              \tag{8}
\]

The ORIGINAL closures, with unrestricted marked cap and actual pivot,
are
\[
 m f(\Omega)p=f(c_0)=\alpha_0,\qquad \phi(f)=\alpha_d .
 \tag{9}
\]
Their proof and original \(N\) factors are in the circle sewing note,
section 3. Both are unit coordinate rows in (6), so have dual norm
EXACTLY one. No arbitrary local marked cap was replaced by an
ordinary cap. Any physical exterior can still be attached before
using (4); it is a full operator identity.

## 4. Explicit twist matrices, their physical star, and coherent sewing

In Newton coordinates multiplication by \(z\) is the real LOWER
bidiagonal matrix
\[
 Z_{rr}=c_r,\qquad Z_{r+1,r}=-|1-Q^{r+1}|^2,\qquad
 Z^T=P_{\rm rev} ZP_{\rm rev}.                           \tag{10}
\]
Every literal signed crossing power acts by
\[
 T_p=R(Z)^p,\qquad R=\kappa r_N,\quad
 \kappa=q^{d^2/2}.
 \tag{11}
\]
Its nodal values and first derivatives are the original complete
ones, with no Jordan term omitted. In particular its all-entry form is
\[
 (T_p)_{ij}
   =\left(\prod_{k=j+1}^i b_k\right)
                 R^p[c_j,\ldots,c_i]\quad(i\geq j);
 \qquad (T_p)_{ij}=0\quad(i<j).                          \tag{12}
\]

One can also use the entirely finite Newton alphabet
\[
 R=\kappa\sum_{r=0}^d(-q)^r\widehat B_r,\qquad
 R^{-1}=\kappa^{-1}\sum_{r=0}^d(-q)^{-r}\widehat B_r .
 \tag{13}
\]
These follow from the literal cup-slide
\(R_{23}^{-1}p=N\kappa^{-1}e_d\), equivalently
\(R_{23}e_d=\kappa p/N\), and (8); that original-source identity is
proved in [the normalization packet](actual_terminal_source_normalization_packet.md).
Equations (11)--(13) retain the common Cartan scalar.

There is a simpler ALL-ENTRY one-crossing kernel. Define the positive
sine Gaussian
\(\beta_{ij}=s_i/(s_js_{i-j})\), \(0\leq j\leq i\leq d\), and
\(\nu_j=(-1)^jq^{j(j+1)}\). Then
\[
 \boxed{\quad
 (T_1)_{ij}=\kappa\nu_j(-q)^{i-j}{i\brack j}_Q
       =\kappa(-1)^iq^{\,i(j+1)}\beta_{ij},\qquad
 (T_{-1})_{ij}=\overline{(T_1)_{ij}}\quad(i\geq j),
 \quad}                                                  \tag{13a}
\]
with zero entries above the diagonal. This includes ALL confluent
channels; it is not an eigenline expansion.

Here is an independent finite proof. Call the first displayed
triangular matrix \(C\). Its first column is
\(\kappa(-q)^i\), exactly \(R(Z)e_0\) by (13).
For \(i\geq j\), Gaussian factorial cancellation gives
\[
 b_i\frac{C_{i-1,j}}{C_{ij}}
   =-q^{-1}Q^{-i}(1-Q^i)(1-Q^{i-j}),\qquad
 b_{j+1}\frac{C_{i,j+1}}{C_{ij}}
   =q^{-1}(1-Q^{j+1})(1-Q^{i-j}).
\]
Their difference is \(-(c_i-c_j)\), so \(CZ=ZC\). The boundary
terms vanish by their displayed factors. Since \(e_0\) is cyclic for
the irreducible lower-bidiagonal \(Z\), two commuting matrices that
agree on \(e_0\) agree on the whole space. Thus \(C=R(Z)\), with no
separation of repeated nodes. Finally
\({i\brack j}_Q=q^{j(i-j)}\beta_{ij}\) proves the second expression
in (13a), and \(R^\sharp=R^{-1}\) proves the inverse.

Thus an arbitrary genuine rational circuit has an explicit alphabet:
unitary reversal, the lower sine-binomial kernel (13a), and its
coefficient conjugate. Its oscillation is the ORIGINAL half-clock
\(q^{ij}\); replacing it by \(Q^{ij}\) would change the source.
Its absolute entry also has the exact angle identity
\[
 \beta_{ij}=N\,w_d(j,i-j,d-i),\qquad
 w_d(a,b,c)=\frac1{s_as_bs_c},\quad a+b+c=d.              \tag{13b}
\]
This follows from \(s_is_{d-i}=N\). It supplies one actual
angle-simplex amplitude with its phase and incidence labels.
It is the amplitude \(Nw_d\), NOT its square root. Any proposed
square-root-energy comparison must still prove its metric and
source compensation rather than silently replacing (13a).

Two adjacent crossings have a further COHERENT all-input elimination:
with \(m=i-j\),
\[
 \boxed{\quad
 (T_2)_{ij}=\kappa^2\nu_j^2(-q)^m {i\brack j}_Q
                           (Q^{j+1};Q)_m
   =\kappa^2\nu_j^2(-q)^m
                           \frac{F_i^2}{F_j^2F_m},
 \quad i\geq j .\quad}                                  \tag{13c}
\]
The negative two-crossing kernel is its coefficient conjugate.
To prove it, expand the actual product \(T_1T_1\), use
\({i\brack k}_Q{k\brack j}_Q
 ={i\brack j}_Q{m\brack k-j}_Q\), and set \(r=k-j\).
The remaining sum is exactly
\[
 \sum_{r=0}^m {m\brack r}_Q
       (-1)^rQ^{r(r-1)/2}(Q^{j+1})^r=(Q^{j+1};Q)_m .
\]
This finite identity follows by inserting the last Pochhammer factor
and the Pascal recursion. Every index is below \(N\). Its cancellations
are retained BEFORE taking an absolute value. Thus the all-entry
magnitude is \(s_i^2/(s_j^2s_{i-j})\), not a sum of positive
one-crossing path magnitudes.

Equivalently, for \(D_F=\operatorname{diag}F_i\) and
\(D_\nu=\operatorname{diag}\nu_i\),
\[
 T_2=\kappa D_F T_1D_F^{-1}D_\nu .                       \tag{13d}
\]
This is a typed packet identity preserving arbitrary adjoining input
and output arrays. Its factorial gauge is on the NEWTON register;
it is not an unrecorded physical-head gauge. Although its endpoint
factors at \(0,d\) are only \(1,N\), its interfaces with a turn must
remain explicit:
\(P_{\rm rev}D_FP_{\rm rev}=ND_\nu D_F^{-1}\).
Consequently (13d) alone is not a polynomial-cost global
replacement of every twist/turn network.

At a real node the original ratio \(R'(c)/R(c)\) is purely imaginary,
and its value has modulus one. Hence full Hermite uniqueness gives
\(R^\sharp=R^{-1}\), not only equality of distinct nodal values.
For ANY multiplication coupon \(M_f\), its exact adjoint in (6) is
\[
 M_f^\dagger=\mathscr R M_{f^\sharp}\mathscr R .
\]
Indeed the Frobenius pairing is symmetric and (4)--(5) imply its
turn is selfadjoint and orthogonal. In particular
\[
 \boxed{\qquad
 \mathscr R^\dagger=\mathscr R,\qquad
 T_p^\dagger=\mathscr R T_{-p}\mathscr R .
 \qquad}                                                \tag{14}
\]

The turn is unitary; the crossing is GENERALLY NOT. Its real
bidiagonal Casimir is nonnormal and has repeated-node derivative
channels. Thus unit nodal phases do not bound a whole twist/word
norm polynomially. Formula (14) is the required typed interface,
not an assertion that every plane-reflected diagram supplies it.

For an arbitrary genuine two-port word \(W\), starting with \(1\),
the original numerator closure now has the exact source Cauchy bound
\[
 |m\,W(1)(\Omega)p|^2\leq\|W(1)\|_{\rm Newt}^2 .         \tag{15}
\]
All internal turns in this energy are the fixed unitary reversal
and all twist kernels are the known matrices (12). No terminal word
or unknown invariant is used to define the metric.

## 5. An exact positive class with genuine extra turns

Let \(A\) be ANY finite typed word in genuine turns and signed crossing
multiplications. Form its ADJOINT WORD by reversing the order and
using the exact replacements (14). It is again a literal rational
tangle circuit with the original turns and signed crossings.
The ORIGINAL numerator closure of its doubled circuit satisfies
\[
 \boxed{\qquad
 m\,[A^\dagger A(1)](\Omega)p
       =\langle1,A^\dagger A1\rangle_{\rm Newt}
       =\|A1\|_{\rm Newt}^2>0 .
 \qquad}                                                \tag{16}
\]
All generators of \(A\) are invertible, so the strict inequality
holds at EVERY level. A recorded outer framing or component
enhancement unit may multiply this raw positive scalar; its
modulus is unchanged.

This class includes words with arbitrary numbers of genuine internal
turns, for instance \(A=T_p\mathscr R T_q\). Its doubled word is
\(\mathscr R T_{-q}\mathscr R T_{-p}\mathscr R
 T_p\mathscr R T_q\), with no unjustified crossing/turn commutations.
Thus the positivity is for an actual specified entire source circuit,
not one expanded crossing state or an arbitrary positive model.

As a calibration, the normalization packet's exact
\(R_{23}p\) formula gives
\[
 R^2=\kappa^2\sum_{r=0}^d(-q)^rF_r\widehat B_r .
\]
Taking \(A=T_2\) in (16) therefore gives \(\sum_rs_r^2\),
the already proved whole-source figure-eight scalar. The general
statement (16) is not inferred from that one example.

For longer \(A\), the energy in (16) retains coherent cancellations
INSIDE \(A1\); the norm only reflects the second half afterwards.
Bounding it by independent absolute-entry capacities would lose the
very coupling this construction preserves. A sharp Rivin-constrained
bound or a nonzero geometric saddle for these arbitrary half-networks
is still needed for a new volume-equality family. This note proves
the all-exterior positive kernel and a genuine full-source
noncancellation operation, not that remaining geometric estimate.

## 6. A complete-circle reflected source with a proved exponent

The known complete packet \(z_N=\mathscr R(R^{-1}L_N)\) now gives
an ENTIRE positive original source with an explicit exponential rate:
\[
 E_N:=\phi(z_N^\sharp\mathscr Rz_N)=\|z_N\|_{\rm Newt}^2,
 \qquad
 \boxed{\ \lim_{N\to\infty}\frac1N\log E_N=\frac{v_8}{\pi}\ } .
 \tag{17}
\]
In particular the original quantum scaling gives rate \(2v_8\).
This uses the already proved actual finite coefficient/endpoint
theorems, rather than a guessed positive envelope. Write
\[
 z_N=N^2\sum_{r=0}^{M} b_{N,r}B_r,\quad
 |b_{N,r}|=\frac{s_{2r}}{s_r^6}|U_r|,\quad M=\lfloor d/2\rfloor.
\]
The exact norm is
\[
 E_N=N^4\sum_{r=0}^{M}\frac{s_{2r}^2}{s_r^8}|U_r|^2 .
 \tag{18}
\]
The [all-index original-source estimate](actual_pretzel_all_index_backward_envelope.md)
gives \(|U_r|\leq CN^B\exp[N\mathcal E(\pi r/N)]\), with
\[
 \mathcal E(u)=\frac2\pi\int_u^{\pi/4}\log\cot v\,dv
       \quad(0\leq u<\pi/4),\qquad \mathcal E(u)=0\ (u\geq\pi/4).
\]
Uniform sine-factorial bounds, INCLUDING both endpoints, give the
remaining exponential profile
\[
 T(u)=\{8\Lambda(u)-2\Lambda(2u)\}/\pi,\qquad
 T'(u)=4\log\cot u/\pi .
\]
Hence \(T+2\mathcal E\) is exactly constant \(j_0=v_8/\pi\) below
\(\pi/4\), and \(T\) decreases above \(\pi/4\). The polynomial number
of summands and their uniform polynomial errors prove the upper
bound in (17). For each FIXED \(u\in(\pi/4,\pi/2)\), the nonzero
coherent high-index asymptotic in
[the complete packet theorem](actual_pretzel_coherent_circle_and_period_asymptotic.md),
section 2 equation (3), gives \(|U_{\lfloor Nu/\pi\rfloor}|^2
\to\sin u>0\). Its one positive summand proves a lower rate \(T(u)\).
Let \(u\downarrow\pi/4\) AFTER the quantum limit to obtain (17).
Both parities and all composite levels are covered.

The actual raw diagram is specified without an unverified link name:
\[
 \boxed{\qquad
 E_N=\phi\!\left(\mathscr R(RL_N)\,R^{-1}L_N\right).
 \qquad}                                                \tag{19}
\]
Here \(\mathscr R\) commutes with coefficient reflection by (4), and
\(L_N^\sharp=L_N\); thus (19) follows from the literal signed boxes,
not a replacement by a positive model. It has two ordinary complete
crossing-circle components. Deleting those two components leaves
the genuine diagram \(\phi(\mathscr R(R)R^{-1})
=\phi(R^{-2})\): the quarter-turn of the single crossing is the
opposite single crossing, and the two-strand closure has two main
components. Thus the complete reflected diagram has FOUR components.
It must not be identified with the three-component Borromean rings
merely from the numerical value \(2v_8\). A face/cusp/topological
identification of its complement is a separate geometric task.
The original single-cut normalization comparison changes only the
recorded unit phase (or the optional one-cut modified factor \(1/N\)),
so it does not alter (17).

Audit: [literal turn, full Newton/Frobenius packet, signed star and reflected original sources](../experiments/audit_actual_newton_turn_positive_gram.py).

Independent analytical review and a fresh audit replay checked the
full physical turn, repeated-node minimal polynomials, extremal-path
normalization, complete Frobenius divisibility, unit original closures,
and the full-Cartan adjoint. The complete-packet rate proof in section 6
was independently re-derived. These checks do not identify the
four-component reflected diagram geometrically or prove a sharp
energy bound for arbitrary words.
