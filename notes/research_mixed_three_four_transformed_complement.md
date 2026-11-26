# The three/four complementary remainder in retained-leg coordinates

Research deduction, 7 November 2026. The completed ordinary pair's
complementary contour has a useful bound after its actual inverse
boundary transform. Performing that transform inside the finite source
replaces the terminal polynomial by the conditional kernel itself.
This removes one endpoint norm from the preceding positive-row bound.
Every physical row, product zero and original boundary derivative is
retained. The whole transformed prefix and its calibrated comparison
remain separate. No numerical evaluation or replay is used.

## 1. The exact inverse boundary transform

Keep the original notation
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\qquad
 C_{1,N}(X,Y)=\sum_{j<N}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
                                                               \tag{1}
\]
All denominator products are nonzero. If \(v(w)\) is the original
Newton column and \(S\) is the change of basis in
[exact wire contraction](research_mixed_wire_exact_contraction.md),
equation (13), then
\[
 b_j(w)=(Sv(w))_j=H_N(w,r^{-j})/P_j.
                                                               \tag{2}
\]
Use the literal cap and terminal polynomial of
[the ordinary pair source](research_mixed_three_four_ordinary_pair_target.md):
\[
 U_{0,N}(w,X)=\sum_{j<N}b_j(w)p_j(X),\qquad
 V_{1,N}(w,X)=\sum_{i<N}\frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i).
                                                               \tag{3}
\]
The normalized retained-leg prefix is
\[
 f_{34,N}(w,Y)=N\operatorname{CT}_X
                         [U_{0,N}(w,X)C_{1,N}(X,Y)].
                                                               \tag{4}
\]
It is exactly \(\mathcal T_{01}U_{0,N}\) in the
[message bridge](research_mixed_conditional_fourier_message_bridge.md),
with degree less than \(N\) in both \(w\) and \(Y\).
The integrated first type is three, so (4) has no \(d_N(X)\)
or additional \(X^{-N}\) sector.

**Lemma 1.** At both parities, for all complex ordinary colors and
all nonzero \(X\),
\[
 V_{1,N}(w,X)=\sum_{b<N}C_{1,N}(X,r^b)b_b(w),\qquad
 E_{34,N}(w,z)=\kappa_N^3N\sum_{b<N}f_{34,N}(w,r^b)b_b(z).
                                                               \tag{5}
\]

*Proof.* The finite identities
\[
 U_{1,N}(w,r^i)=\sum_{b<N}\frac{b_b(w)p_b(r^i)}{P_b},
 \qquad \frac{p_b(r^i)}{P_b}=\frac{p_i(r^b)}{P_i}
                                                               \tag{6}
\]
retain the exact zero when \(i+b\ge N\). Insert (6) into
(3) and interchange the finite sums to obtain the first identity.
Inserting it into the original
\(\kappa_N^3N^2\int_0^1U_0(w,X)V_1(z,X)\,da\),
where \(X=e^{-2\pi ia}\), gives the second. The increasing
\(a\) integral extracts the constant coefficient. No extra
factorial, Gram matrix or node normalization is inserted. \(\square\)

Let \(c\) be the unchanged complete-pair attached height from
[complementary-contour completion](research_mixed_three_four_complementary_contour_completion.md).
Its sole frozen saved input gives
\[
                         -7/200<c<0.                  \tag{7}
\]
The saved result has SHA256
fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70.
No action value is needed for the absolute bound below.
Let \(\Gamma_+\) run upward from \(1/2+ic\) to \(1/2\),
then along the real interval to one. Define
\[
\begin{split}
 I_{+,N}(w,z)&=\kappa_N^3N^2\int_{\Gamma_+}U_{0,N}(w,X)V_{1,N}(z,X)\,da,\\
 f_{+,N}(w,Y)&=N\int_{\Gamma_+}U_{0,N}(w,X)C_{1,N}(X,Y)\,da.
\end{split}                                                     \tag{8}
\]
These are open-contour integrals, not partial physical-root sums.
Writing \(I_{+,N}(w,z)=\mathbf e_+(w)^Tv(z)\), and writing
\(\mathbf f_+(w)=(f_+(w,1),f_+(w,r),\ldots,f_+(w,r^{N-1}))\)
as a row, equation (5) proves
\[
 \mathbf f_+(w)=(\kappa_N^3N)^{-1}\mathbf e_+(w)^TS^{-1},
 \qquad
 I_{+,N}(w,z)=\kappa_N^3N\sum_{b<N}f_{+,N}(w,r^b)b_b(z).
                                                               \tag{9}
\]
Its \(Y\)-degree is less than \(N\), so the full original node
set determines this polynomial exactly. Ordinary derivatives still
differentiate the polynomials \(b_b(z)\) in (9); raw normal
observations have not been replaced by simple-node observations.
The same formulas apply to the complete source.

The other incoming path \(\Gamma_-\) in the ordinary proof
defines \(f_-\) with the same integrand. Entire periodicity gives
\[
                        f_{34,N}=f_{-,N}+f_{+,N}.       \tag{10}
\]
Bounds for the ordinary first-path contribution do not, by themselves,
bound \(f_-\) after this inverse transform.

## 2. Whole-row estimates on the closed outgoing disk

Set
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\quad
 L(t)=-2J((1-t)/2),\quad B_0=1549/1500.
                                                               \tag{11}
\]
Equation (10) of
[complementary real colors](research_mixed_three_four_complementary_real_colors.md)
proves, for every prescribed tolerance,
\[
 \sup_{w\in[-2,2]}|U_{0,N}(w,e^{-2\pi i(x+ih)})|
       \le C_\tau N^{B_\tau}e^{N(B_0+\tau)}
       \quad(1/2\le x\le1,\ c\le h\le0).
                                                               \tag{12}
\]
This keeps the whole endpoint coefficients, both extreme private
layers and all revived numerator rows.

The original centered-arc numerator bound, used also in Section 3
of [the full boundary theorem](research_mixed_three_four_full_boundary_kernel.md),
and the polynomial maximum principle give
\[
 \sup_{|Y|\le1}|p_j(Y)|
   \le C_\tau N^{B_\tau}e^{N\{L(t)+\tau\}},
                 \qquad t=j/N,\quad 0\le j<N.
                                                               \tag{13}
\]
The maximum principle adds no rate to the unit-circle bound.
This includes \(Y=0\), all product zeros and both true row endpoints.

For \(a=x+ih\), put
\[
 I_{x,h}(t)=\int_0^t
              \log|1-e^{2\pi h}e^{-2\pi i(x+u)}|\,du.
                                                               \tag{14}
\]
The complete positive-row rate of \(U_0C_1\), using (12)--(13),
is
\[
                  B_0+L(t)-3J(t)+I_{x,h}(t)-2\pi ht.
                                                               \tag{15}
\]
This is the old complementary rate with \(b_1=433/500\)
removed: its extra complete endpoint coefficient is absent in (1).
No bound is divided by that coefficient or by a finite zero.

On the real far half the exact integral comparison is
\[
 I_{x,0}(t)\le
 \begin{cases}
 -J(1/2-t),&0\le t\le1/2,\\
 J(t),&1/2\le t\le1.
 \end{cases}
                                                               \tag{16}
\]
The already proved direct scalar bounds in complementary-contour
completion, equations (11)--(14), are
\[
 \max_{t\le1/2}[L(t)-J(1/2-t)-3J(t)]<377/500,\qquad
 \max_{t\ge1/2}[L(t)-2J(t)]<73/250.
                                                               \tag{17}
\]
Thus the two real-half ceilings in (15) are \(134/75\) and
\(1987/1500\).

On the vertical segment set \(\delta=-2\pi h<11/50\).
Equations (16)--(22) of that source retain the exact radius
identity and original chirp and prove
\[
 L(t)-3J(t)+I_{1/2,h}(t)+\delta t
       <377/500+11/300+7/1920
                         \quad(0\le t\le1/2).
                                                               \tag{18}
\]
The proof first treats \(t\le1/3\), then proves strict decrease
on \([1/3,1/2]\); it does not omit those rows.
For \(t\ge1/2\), the same source proves \(I_{1/2,h}(t)\le0\).
Using \(J(t)\ge0\), \(L(t)<1/3\), and
\(\delta t<11/50\) gives ceiling
\(B_0+1/3+11/50=793/500\).
The largest displayed ceiling is therefore
\[
 C_+=B_0+377/500+11/300+7/1920=17539/9600.
                                                               \tag{19}
\]
Uniform zero-safe products and denominator factorial bounds retain
all \(j=0,\ldots,N-1\), including exact or revived zeros.
Choose their aggregate error within one arbitrary \(\tau>0\).
The row count, \(N\) in (8), and fixed path length cost only
polynomial factors.

**Theorem 2.** For every \(\tau>0\), fixed \(k,\ell\ge0\)
and compact \(K\subset\mathbb C\),
\[
 |\partial_w^k\partial_Y^\ell f_{+,N}(w,Y)|
 \le C_{k,\ell,\tau,K}N^{B_{k,\ell,\tau,K}}
       e^{N\{C_++\log_+|Y|+\tau\}},
              \qquad w\in[-2,2],\quad Y\in K.
                                                               \tag{20}
\]
Both level parities are included. This is an absolute derivative
estimate, not a logarithmic derivative or normalized symbol bound.

*Derivative proof.* Apply Markov in the real ordinary variable
to the complete \(U_0\) bound (12), before the positive row sum;
a fixed order \(k\) costs \(CN^{2k}\). The result has
\(Y\)-degree at most \(N-1\). A degree-\(D\) polynomial
outside the unit disk grows by at most \(|Y|^D\) times its
disk supremum. About a point \(Y\), put \(R=\max(1,|Y|)\)
and apply Cauchy on a circle of radius \(R/N\). The larger
radius costs only \((1+1/N)^{N-1}<e\), in addition to
\(R^{N-1}\); the derivative costs at most \(CN^\ell\).
This proves (20), including on \(|Y|=1\), without logarithmic
differentiation at a zero. \(\square\)

## 3. The sharper scalar that retains the actual output

Instead of (13), retain
\[
                  I_Y(t)=\int_0^t\log|1-Ye^{-2\pi iu}|\,du.
                                                               \tag{21}
\]
It is jointly continuous on compact \(Y,t\) sets, including
zeros, by integrability of the local logarithmic singularity.
Let \(J_{\rm far}(t)=-J(1/2-t)\) for \(t\le1/2\)
and \(J_{\rm far}(t)=J(t)\) for \(t\ge1/2\).
With \(\delta_*=-2\pi c\), define the explicit scalar
\[
\begin{split}
 \mathcal R_+(Y)=B_0+\max\big\{&
 \max_{0\le t\le1}[I_Y(t)-3J(t)+J_{\rm far}(t)],\\
 &\max_{\substack{0\le t\le1\\0\le\delta\le\delta_*}}
   [I_Y(t)-3J(t)+I_{1/2,-\delta/(2\pi)}(t)+\delta t]\big\}.
\end{split}                                                     \tag{22}
\]
The pieces agree at their joining index. Uniform zero-safe
finite products prove, on each compact \(K\),
\[
 |\partial_w^k f_{+,N}(w,Y)|
 \le C_{\tau,K}N^{B_{\tau,K}}e^{N\{\mathcal R_+(Y)+\tau\}},
                   \qquad w\in[-2,2],\quad Y\in K.
                                                               \tag{23}
\]
The same statement holds for fixed outgoing derivatives after
allocating an arbitrary extra rate tolerance: use Cauchy on a
fixed small complex neighborhood and uniform continuity of (22).
Equations (13)--(19) show
\(\mathcal R_+(Y)\le C_+\) on \(|Y|\le1\).
This comparison retains the actual output radius and angle.

## 4. The original context calibration, and what is still missing

For precision, use a new notation for the phase of (4). It is
not the phase of a prefix with an additional final Gram matrix
or Fourier observation. Fix the actual following external leg in
an open word of length at least three, so its second vertex is
ordinary, and use the one-ended critical family in Section 2 of
[open boundary comparison](research_mixed_open_boundary_comparison_reduction.md).
For its first two types \(3,4\), the bare conditional phase is
\[
 Q(s;a,z)=g(s+a)+g(s+z)-3g(s)-g(a)-g(z)+2\pi ias.
                                                               \tag{24}
\]
Let \(T_0\) be the original calibrated first-cap phase, and set
\[
 \mathcal P^{\rm bare}_{34}(z)=
 [T_0(a)+Q(s;a,z)]_{\partial_a(T_0+Q)=0,\ Q_s=0},
 \qquad
 \mathcal L_{34}(z)=\mathcal P^{\rm bare}_{34}(z)-g(z)/2.
                                                               \tag{25}
\]
The original local source packets identify this phase and its
nonzero local current at the actual reference. This says nothing
about the rest of the complete \(f_{34}\).
Stationarity of the eliminated variables gives the exact first
marginals
\[
 (\mathcal P^{\rm bare}_{34})'(z_*)=g'(s_*+z_*)-g'(z_*),
 \qquad
 \mathcal L_{34}'(z_*)=g'(s_*+z_*)-\tfrac32g'(z_*).
                                                               \tag{26}
\]
All primitives and logarithmic lifts are the original ones.
The subtraction in (25) allocates one unselected output halfweight.
It is not deduced by differentiating (20).

The actual geometric output here belongs to \(O_4\) of
[the ordinary reference domains](research_mixed_actual_last_row_reference_domains.md),
equation (1), by the original whole-map image bound and its open-word
inheritance. Thus \(\Im z_*<-1/1000<0\), hence
\(|e^{-2\pi iz_*}|<1\). This assertion concerns those actual outputs,
not every point of a containing typed disk. For a horizontal target
\(z=x+i\Im z_*\) in the original Fourier-weight domain,
an explicit sufficient comparison of this remainder with the
actual allocated boundary plane is
\[
\begin{split}
 \mathcal R_+(e^{-2\pi iz})-\tfrac12\Re g(z)
 <{}&\Re\mathcal L_{34}(z_*)
      +\Re\mathcal L_{34}'(z_*)(x-\Re z_*)\\
    &-\kappa_*(x-\Re z_*)^2,\qquad\kappa_*=1/2500000.
\end{split}                                                     \tag{27}
\]
The existing Fourier-weight theorem applies here to the actual
polynomial \(d_N\); no finite square root or division is needed
in this modulus inequality. At the reference, (27) reduces to
\[
          \mathcal R_+(e^{-2\pi iz_*})
                         <\Re\mathcal P^{\rm bare}_{34}(z_*).
                                                               \tag{28}
\]
Replacing \(\mathcal R_+\) by \(17539/9600\) is a stronger
sufficient scalar test. Neither test is asserted on the whole
actual reference family by this note.

At the next exact gluing the output type four carries the entire
factor \(d_N(Y)(1+Y^{-N})\). Both summands must remain, with
their own moduli and their original allocation. The halfweight
comparison (27) treats only its stated unselected allocation;
it does not delete the selected sector or infer its sign.
For positive outgoing height the general bound (20) pays the
explicit additional \(2\pi(\Im z)_+\).

Thus the entire previously proved complementary source has been
transferred to the required retained-leg representation with a
concrete absolute ceiling and a sharper output-dependent scalar.
The transformed first path in (10), the context inequalities
(27)--(28), further selections and the final observed coefficient
remain separate. No new knot family is claimed.
