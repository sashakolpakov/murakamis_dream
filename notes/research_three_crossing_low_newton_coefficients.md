# Low Newton coefficients of the complete three-crossing pair

Research proof, 7 November 2026.

The original pendant \(33\) proof is stable under an initial interval
of Newton coefficient insertions. This is a statement about the
complete finite source, including its coherent real-index removals
and every contour current. It does not follow from the value at the
single node \(c_0\).

The useful insertion is the single Newton polynomial \(e_b(C)\).
It gives the coefficient itself, so no divided-difference estimate
or replacement of a repeated-root normal is needed.

## 1. Source and statement

Use the original conventions
\[
 \begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=e^{\pi iD^2/(2N)},\\
 S_m=\prod_{r=1}^m2\sin(\pi r/N),\quad
 c_m=qQ^m+q^{-1}Q^{-m},\\
 e_m(w)=S_m^{-2}\prod_{r<m}(c_r-w),\quad
 v(w)=(e_0(w),\ldots,e_D(w))^T,\quad A_3=JM^3 .
 \end{gathered}                                                   \tag{1}
\]
Coordinate vectors are denoted \(\mathbf e_b\), to distinguish
them from the polynomials \(e_b\). Define the exact row
\[
 \ell_b(w)=v(w)^TA_3^2\mathbf e_b,\qquad
 E_{33}(w,t)=\sum_{b=0}^D\ell_b(w)e_b(t).                         \tag{2}
\]
In particular \(\ell_0\) is exactly the pendant source \(F_N\)
in the [full boundary theorem](research_three_crossing_full_boundary_asymptotic.md).
Let \(\mathcal W(w)\) be its holomorphic action near \(w=-2\),
and put \(M_{\rm pend}=\Re\mathcal W(-2)\).

**Theorem 1.** There is a function \(\varepsilon(\delta)\to0\)
as \(\delta\downarrow0\) such that, for every sufficiently small
fixed \(\delta>0\) and every \(\tau>0\), the following estimates
hold for all \(0\le b\le\lfloor\delta N\rfloor\):
\[
 |\ell_b(-2\cos u)|
 \le C_{\delta,\tau}N^{A_{\delta,\tau}}
 \exp N\left[
 M_{\rm pend}-\frac{1-\cos u}{4000}
                 +\varepsilon(\delta)+\tau\right],
 \qquad -\pi\le u\le\pi.                                       \tag{3}
\]
On a fixed sufficiently small ordinary complex disk about \(-2\),
\[
 \left|e^{-N\mathcal W(w)}\ell_b(w)\right|
 \le C_{\delta,\tau}N^{A_{\delta,\tau}}
                  e^{N[\varepsilon(\delta)+\tau]}.             \tag{4}
\]
The disk in (4) can be chosen independently of \(\delta\).
Every fixed ordinary derivative satisfies (3) with its angular
loss omitted and a polynomially enlarged prefactor. On smaller
fixed disks, every fixed derivative of the normalized expression
in (4) satisfies the same bound. All assertions include both
parities and all original coefficient coordinates.

Thus for every \(\eta>0\), a fixed positive \(\delta\) can be
chosen so that the complete low coefficient interval has rate
at most \(M_{\rm pend}+\eta\), uniformly over all real ordinary
boundary colors. This is an upper bound, not a nonzero
asymptotic for any inserted source.

## 2. Exact insertion and the prepared amplitude

Let \(C\) denote multiplication by the ordinary spectral variable
in the original Newton basis. The
[coefficient transport identity](research_complete_boundary_coefficient_transport.md),
equation (7), gives
\[
 C_{mm}=c_m,\qquad C_{m,m-1}=-s_m^2,\qquad
 s_m=2\sin(\pi m/N).                                           \tag{5}
\]
In particular \(\|C\|_2\le6\), because its maximum absolute row
and column sums are at most \(6\). Since \(C\) and \(M\) are
multiplication operators in the same full quotient algebra,
they commute. The normalized Newton recurrence gives exactly
\[
 e_b(C)\mathbf e_0=\mathbf e_b .
\]
Indeed the factors \(c_r-C\) successively move the leading
coordinate from \(r\) to \(r+1\), with multiplier \(s_{r+1}^2\);
their product is canceled by \(S_b^2\). Therefore
\[
 \boxed{\quad
 \ell_b(w)=v(w)^TJM^3J\,e_b(C)\alpha,\qquad
 \alpha=M^3\mathbf e_0 .
 \quad}                                                        \tag{6}
\]
This uses actual finite matrix multiplication, including the
nilpotent parts at double roots.

The [original preparation](research_three_crossing_prepared_boundary_sum.md)
is
\[
 \alpha=\kappa^3A_Nh+\delta_N,\qquad
 h_m=q^{m(m+2)}S_m^2,\quad
 \|\delta_N\|_2=O(N^{3/2}),\quad |A_N|=O(N^{-1/2}).              \tag{7}
\]
Put \(z_m=qQ^m\). For a polynomial \(a\), write
\((\mathsf T a)_m=a(z_m)h_m\), and define
\[
 (\mathscr C a)(z)
       =(z+z^{-1})a(z)-z^{-1}a(Q^{-1}z).                        \tag{8}
\]
This is again a polynomial: on a monomial,
\[
 \mathscr C z^k=z^{k+1}+(1-Q^{-k})z^{k-1},
\]
where the second term is zero when \(k=0\). A direct calculation
using \(s_m^2h_{m-1}/h_m=z_m^{-1}\) proves
\[
 C\mathsf T a=\mathsf T\mathscr C a
                         +q^{-1}a(q^{-1})\mathbf e_0 .          \tag{9}
\]
In particular \(Ch=(z_mh_m)_m+q^{-1}\mathbf e_0\).

Define unnormalized polynomials and remainder vectors by
\[
 \begin{gathered}
 a_0=1,\quad r_0=0,\\
 a_{b+1}=(c_b-\mathscr C)a_b,\qquad
 r_{b+1}=(c_b-C)r_b-q^{-1}a_b(q^{-1})\mathbf e_0 .
 \end{gathered}                                                 \tag{10}
\]
Induction in (9) gives the exact identity
\[
 e_b(C)h=\mathsf T\mathcal A_b+\mathfrak r_b,\qquad
 \mathcal A_b=a_b/S_b^2,\quad \mathfrak r_b=r_b/S_b^2.           \tag{11}
\]
Here \(\deg a_b=b\), and \(r_b\) is supported on \(0\le m<b\).
Support alone is not used as an error estimate.

For \(R\ge1\), give a polynomial the coefficient norm
\(\|a\|_R=\sum_k|a_k|R^k\). Equation (8) implies
\[
 \|\mathscr Ca\|_R\le(R+2/R)\|a\|_R,\qquad
 \|a_b\|_R\le(2+R+2/R)^b .                                    \tag{12}
\]
At \(R=1\) the last bound is \(5^b\). Also
\(\|c_b-C\|_2\le8\), so (10) gives
\[
 \|r_b\|_2\le b\,8^{b-1}\quad(b\ge1),\qquad
 \|e_b(C)\|_2\le8^b/S_b^2.                                    \tag{13}
\]
These estimates are uniform in the level.

Choose a fixed \(R\ge1\) which contains
\(q^{-1}e^{-2\pi iz}\) on every old retained product contour
and on a fixed small neighborhood of the selected contour
deformation. Let
\[
 B=\max\{16,\,2+R+2/R\},\qquad
 \epsilon_B(\delta)=
          \delta\left[\log B+2+2\log(1/\delta)\right].           \tag{14}
\]
For \(b\le\delta N\), \(\delta<1/2\), the elementary chord bound
\[
 S_b\ge(4/N)^b b!
\]
and \(b!\ge(b/e)^b\) show
\[
 B^b/S_b^2\le e^{N\epsilon_B(\delta)}.                          \tag{15}
\]
For \(b=0\) this means \(1\le1\). For positive \(b\), the
function \(s[\log B+2+2\log(1/s)]\) is increasing on
\(0<s\le1/2\), which justifies its evaluation at \(\delta\).
Discarding the favorable factor \(4^{-2b}\) only weakens
the estimate.

Combining (7), (11), and (13), the exact inserted preparation is
\[
 e_b(C)\alpha
   =\kappa^3A_N\mathsf T\mathcal A_b+\rho_{N,b},\qquad
 \|\rho_{N,b}\|_2\le C N^{3/2}
                              e^{N\epsilon_B(\delta)}.         \tag{16}
\]
Thus the boundary forcing in (9) and the original preparation
error are both controlled in the original coefficient norm.
The [global preparation-error proof](research_three_crossing_global_preparation_error.md)
applies its remaining operator to any such vector. Its old
rate, strictly below \(3/2\), increases by at most
\(\epsilon_B(\delta)\). This remains true with coordinate
projections, on the full real color interval, and on the
fixed small ordinary complex disk used there.

## 3. The coherent outer removals

The original real \(x,y\) removals are not absolute estimates
of all inner \(k\) summands. They must be retained coherently.
Write
\[
 \gamma=MJ\alpha,\qquad
 \gamma_b=MJ e_b(C)\alpha .
\]
With \(L=JCJ=C^T\), the exact crossing-transport identities give
\[
 T=M L M^{-1}=L_{-1}=J L_1J,\qquad
 \gamma_b=e_b(T)\gamma .                                      \tag{17}
\]
The explicit \(L_1\) in the
[coefficient transport note](research_complete_boundary_coefficient_transport.md),
equation (13), has diagonal modulus at most \(6\) and both
off-diagonal moduli at most \(4\). Hence \(T\) is tridiagonal,
\(\|T\|_2\le14\), and
\[
 \|e_b(T)\|_2\le16^b/S_b^2,\qquad
 (e_b(T))_{ij}=0\quad\hbox{if }|i-j|>b .                        \tag{18}
\]
For a set of physical indices \(I\), let \(I^{+b}\) be its
distance-\(b\) enlargement, clipped to \(\{0,\ldots,D\}\).
The exact identity
\[
 P_Ie_b(T)=P_Ie_b(T)P_{I^{+b}}                                \tag{19}
\]
therefore controls a restricted \(\gamma_b\) using a restricted
original \(\gamma\), at the multiplicative cost (15).

Here is the precise small enlargement needed at the two old
cuts. Use the continuous original functions
\[
 A(x)=\Re I(x)-2\mathcal J(x),\qquad
 B_0(x)=\Re I(x)-\mathcal J(x)
\]
from [the actual next-column theorem](research_three_crossing_next_crossing_fourier.md).
The symbol \(B_0\) here is a function, distinct from the constant
\(B\) in (14). That theorem proves the left endpoint estimate,
the increasing right profile \(B_0\), the global norm rate
\(\max A\), and \(A(1/2)=B_0(1/2)\). Its transfer matrices on
\([2/5,3/5]\) have a fixed norm bound \(K\ge1\).

For \(0<\delta<1/40\), define
\[
 \omega(\delta)=\max\left\{
 0,\ A(1/10+2\delta)-A(1/10),\
 A(1/2-2\delta)+4\delta\log K-B_0(1/2)
                    \right\}.                                \tag{20}
\]
All one-sided values in (20) are continuous, so
\(\omega(\delta)\to0\).
The original critical point of \(A\) is greater than \(1/3\);
therefore \(A\) is increasing on the first interval in (20).
For all sufficiently large \(N\), the enlarged lower index set
lies below \(1/10+2\delta\). For the enlarged upper set, use
the original right endpoint estimate above \(1/2+2\delta\),
and the bounded transfer matrices across the remaining interval.
At most \(4\delta N+O(1)\) transfer steps are needed.
Consequently, for every fixed \(\tau>0\),
\[
 \begin{split}
 \|P_{\{j/N<1/10\}}\gamma_b\|_2
 &\le \operatorname{poly}_{\delta,\tau}(N)
 e^{N[A(1/10)+\epsilon_B(\delta)+\omega(\delta)+\tau]},\\
 \|P_{\{j/N\ge1/2\}}\gamma_b\|_2
 &\le \operatorname{poly}_{\delta,\tau}(N)
 e^{N[B_0(1/2)+\epsilon_B(\delta)+\omega(\delta)+\tau]},\\
 \|\gamma_b\|_2
 &\le \operatorname{poly}_{\delta,\tau}(N)
 e^{N[\max A+\epsilon_B(\delta)+\tau]} .
 \end{split}                                                   \tag{21}
\]
The arbitrarily small \(\tau\) absorbs the uniform endpoint
and transfer \(o(1)\); no new root or profile value is evaluated.

Repeat Section 6 of the global preparation-error note with
(21). Its lower \(x\) tail uses the first line, its upper \(x\)
tail uses the second, and both omitted \(y\) ranges use the
last line. The triangular support of \(JM^2\) is unchanged.
All these complete omitted sums retain their old rates with
an added debit at most
\(\epsilon_B(\delta)+\omega(\delta)+\tau\).
Replacing \(\gamma_b\) by the amplitude-prepared vector in
(16) costs the already controlled projected preparation error.
This justifies the original cuts without asserting an
absolute estimate for an inner coherent sum.

The same argument preserves the additional omitted
\(y\ge13/40\) range at middle boundary angles, and the
far-angle original matrix estimate: both use the full
\(\|\gamma\|_2\) bound, which is replaced by the last line
of (21). This also retains their true endpoint and parity
conventions.

## 4. Every prepared current and both wire tails

The exact prepared formula is equation (4) of the
[prepared-sum theorem](research_three_crossing_prepared_boundary_sum.md).
Replacing \(h_m\) by \(\mathcal A_b(qQ^m)h_m\) multiplies
its \((i,j,k)\) summand by exactly
\[
                \mathcal A_b(qQ^{D-k})
                    =\mathcal A_b(q^{-1}Q^{-k}).                \tag{22}
\]
No index, carrier, factorial, or outside scalar changes.
The equality follows already in the \(MJh\) step of that
proof: the entry being used is \(h_{D-k}\).

At physical indices the multiplier in (22) is bounded
by (15). The two wire removals \(k/N\le1/100\) and
\((j-k)/N\le1/400\) in the
[wire-tail theorem](research_three_crossing_global_horizontal_and_wire_tails.md)
are absolute sums of the original triple summands. Thus
their old rates \(663/500\) and \(18229/12000\) increase
by at most \(\epsilon_B(\delta)\).

On the retained polytope the new exact interpolation is
\[
 f_N(x,y,z;u)\,
                    \mathcal A_b(q^{-1}e^{-2\pi iz}),           \tag{23}
\]
where \(f_N\) is the full original interpolation in equation
(1) of the
[retained-polytope contour theorem](research_three_crossing_retained_polytope_contour.md).
The multiplier is entire in \(z\), and is bounded by (15)
on the chosen fixed contour neighborhood. Apply the original
one-cell identity to (23) before collecting faces. Its
indicator \(\chi_N\), finite differences \(\Delta_V\chi_N\),
residue factors, and half-grid kernels are exactly unchanged.
In particular both slanted staircase sheets remain. There
are no finite differences of the amplitude: face collection
uses the same holomorphic function on the two adjacent cells.

Every one of the eight horizontal integrals and all 144
mixed-current comparisons therefore keeps its old bound,
multiplied by at most \(e^{N\epsilon_B(\delta)}\). The same
is true of all 39 extra currents in the
[whole-period theorem](research_three_crossing_whole_period_source.md):
their altered \(y\) cut changes neither (22) nor the compact
set of \(z\) heights. The old real angular loss applies
pointwise to \(f_N\), while the multiplier is independent
of \(u\). No cancellation of an inserted polynomial is
assumed in any current estimate.

On the principal horizontal, the old phase has maximum
\(M_{\rm pend}\) at \(u=0\), and loses at least
\((1-\cos u)/128\) on the admitted real angular contours.
For complex \(w\) near \(-2\), use the same local deformation
through the continued saddle as in the full boundary theorem.
Its selected local contour has real phase at most
\(\Re\mathcal W(w)\); the complement and the local joining
faces retain a fixed strict gap. The entire multiplier in
(23) remains bounded by (15) there. These facts require
only an upper bound for the integral, not stationary phase
with a slowly varying or nonzero inserted amplitude.

Combining these bounds with (16)--(21) proves (3)--(4), for
example with
\[
                    \varepsilon(\delta)
                       =\epsilon_B(\delta)+\omega(\delta).
                                                                    \tag{24}
\]
The old strict rational gaps absorb the same angular loss
\(1/4000\) as in the whole-period theorem, with the added
debit in (24). Markov's inequality on the full real
ordinary interval gives the stated fixed derivative bound.
The normalized left side of (4) is holomorphic; Cauchy's
formula on nested fixed disks gives its fixed derivatives.
This completes the proof of Theorem 1.

## 5. Nodal insertions and the exact next-transfer scope

For \(j<N/2\), the physical evaluation vector has no entries
above \(j\), because the numerator of \(e_\ell(c_j)\) contains
its \(r=j\) zero when \(\ell>j\). Hence
\[
 E_{33}(w,c_j)=
 v(w)^TJM^3J\,K(c_j,C)\alpha,\qquad
 K(c_j,t)=\sum_{\ell=0}^j e_\ell(c_j)e_\ell(t).                  \tag{25}
\]
Since \(|e_\ell(c_j)|\le4^\ell/S_\ell^2\), equations
(3)--(4) and (15) give the same complete-source estimates
for (25), with the additional vanishing rate debit
\[
 \epsilon_4(\delta)
          =\delta[\log4+2+2\log(1/\delta)] .                   \tag{26}
\]
This proves directly that the proposed low-degree insertion
is tolerated by the pendant proof, including its true
trace currents. It is a consequence of the coefficient
proof, not its premise.

The [exact lowered-word identity](research_mixed_next_lowered_word_dual_observation.md)
gives, with \(r=q^{-2}\) and \(P_b=(r;r)_b\),
\[
 \frac{F_{34}(w,r^b)}{P_b}
              =\frac{(-q)^b}{\kappa^2N}\ell_b(w).               \tag{27}
\]
Thus this entire original coefficient, including its small
factorial divisor, is uniformly controlled for
\(0\le b\le\delta N\). In particular the combined next
transfer restricted to those physical indices is exactly
\[
 \frac1{\kappa^2N}
   \sum_{b=0}^{\lfloor\delta N\rfloor}
                (-q)^b\ell_b(w)C_\beta(r^b,Z).                 \tag{28}
\]
Both original Fourier sectors have been combined in (28)
by the proved finite root identity; neither is separately
estimated here.

To delete (28) below the actual next action one still needs
a uniform bound on \(C_\beta(r^b,Z)\) over this interval.
Its value at \(b=0\), even when exactly evaluated, is not
substituted for the other rows. Likewise a physical-index
deletion would not itself delete an arc of either coefficient
contour. No lower bound, nonzero inserted coefficient,
general short-word closure, or complete next-attachment
asymptotic is asserted.
