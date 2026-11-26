# Outer aliases after the complete private cap is contracted

Research reduction, 7 November 2026. The literal private-index
expansion remains exact at complex outgoing arguments. Bounding its
real private indices, without a private contour deformation, reduces
all horizontal aliases of the three-index prepared source to the six
already paid compact-profile bounds and six explicit true-endpoint
residual bounds. The latter signs are not asserted here. This uses no
extension of the macroscopic complex endpoint rectangle beyond
\(\Re s=.49\), and no new evaluation.

## 1. The expansion is exact at complex \(t\)

Keep the exact three-index source (2) of
[the main-sheet theorem](research_mixed_prepared_cap_three_index_sheet.md).
Its first factor is the literal polynomial
\[
 U_{0,N}(w,X)=\sum_{i=0}^{N-1}
       \frac{\mathcal H_N(w,r^{-i})(rX;r)_i}{P_i}
 =\sum_{i=0}^{N-1}D_N(i/N)^{-1}C_N(i/N,w)(rX;r)_i,
 \qquad X=e^{-2\pi it}.
\tag{1}
\]
The first equality is the original polynomial definition, valid for
every complex \(X\); the second uses the exact physical coefficient
identity \(b_i=D_N(i/N)^{-1}C_N(i/N,w)\). There is no
termination condition \(i+Nt<N\) at a complex \(t\).
In particular the physical-node identity which removes indices beyond
that condition is not used off the grid.

For \(i/N=s\in[.27,.49]\) and \(t_R\in[.22,.5]\),
the original factorial functional equation gives exactly
\[
 (r e^{-2\pi it};r)_i
       =\frac{\widehat P_N(N(t+s))}{\widehat P_N(Nt)}.
\tag{2}
\]
Both real arguments remain strictly between zero and one.
Their original complex heights need not vanish. The coherent
endpoint packet and the exact factorial expansion therefore give
the rate of these retained physical summands as
\[
 \Re\Psi_0(s,t),\qquad
 \Psi_0(s,t)=S(s)+J(s+t)-J(t)-i\pi st.
\tag{3}
\]
Every original chirp and constant is present. No private-index
Gaussian approximation or private alias is needed to upper-bound
the finite sum of these terms.

## 2. A direct whole-cap bound on the common height domain

Use the full target tube
\[
 Z_t=[.22,.5]+i[-.072,.021].
\tag{4}
\]
The original compact physical-tail proof extends to all of (4),
by Section 2 of
[the upper-target cap domain theorem](research_mixed_cap_upper_target_extension.md)
and the type-three part of
[the hybrid-height source envelope](research_mixed_boundary_window_real_color_envelopes.md).
It does not require \(t\) to be a critical point or its height to
equal an attached reference height.

More explicitly, on the real private middle the coherent full-index
coefficient theorem gives the rate
\[
 R_0(s,t)=\Re S(s)+\int_0^s
                 \log|1-e^{2\pi\Im t-2\pi i(\Re t+x)}|\,dx.
\tag{5}
\]
The original monotonicity argument bounds the compact lower and upper
tails by \(R_0(.27,t)\) and \(R_0(.49,t)\), respectively. It
retains the positive-height reflection term
\(2\pi(\Im t)_+s\), and remains valid through the numerator
zeros beyond a physical support wall. At the two retained cuts
(5) is exactly (3). This is a real-index estimate for the literal
products in (1), not a continuation of a triangular support zero.

The true lower index end has rate below \(1/4\). The upper end
uses the exact polynomial identity
\[
 (rX;r)_i=\frac{1-X^N}{\prod_{j=i+1}^{N}(1-r^jX)}
\tag{6}
\]
with its removable continuation. For \(i/N\ge.99\), the
denominator-angle bound and the original zero-safe Newton entropy
give the ceiling
\[
 c_{\mathrm{end}}(h)=
 \max\left\{\frac14,\,
       \frac35+2\pi h_++\frac1{100}\log(40/19)\right\},
 \qquad h=\Im t.
\tag{7}
\]
This is the true-index bound, not the modulus of a canceled
complete-color sum. The same angle bound holds through \(t_R=.5\).
As in Section 3 of
[the completed upper-target theorem](research_mixed_cap_upper_target_completion.md),
\(h_+\le.021\), \(\pi<22/7\), and \(\log(40/19)<4/5\)
prove
\[
                      c_{\mathrm{end}}(h)<\frac{37}{50}.
\tag{8}
\]

Consequently, putting
\[
 A_{\mathrm{real}}(t)=
          \max_{.27\le s\le.49}\Re\Psi_0(s,t),
\tag{9}
\]
the whole literal cap satisfies, for each \(\eta>0\),
\[
 |U_{0,N}(w,e^{-2\pi it})|
 \le C_\eta N^{A_\eta}
       \left[e^{N(A_{\mathrm{real}}(t)+\eta)}
                     +e^{N(37/50+\eta)}\right],
                 \qquad t\in Z_t.
\tag{10}
\]
All physical private indices of (1) are covered: retained middle,
both compact tails, and both true endpoints. The underlying complete
coefficient and zero-safe product bounds give a fixed sufficiently
small ordinary-color neighborhood and all fixed ordinary jets,
with both level parities. The rate tolerance is aggregate, not one
unpaid tolerance for each factor. This bound neither evaluates nor
deforms a complex private index outside the proved rectangle.

## 3. The exact residual factor and its height penalties

Let
\[
\begin{split}
 C_3&=[.22,.5]\times[.2,.42]^2,\\
 H_t&=[-.072,.021],\qquad H_p=H_q=[-.102,.015],\\
 R(t,p,q)&=V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(x_0).
\end{split}
\tag{11}
\]
These are the remaining three-index phase and original source
domains; \(V(a,b)=g(a+b)-g(a)-g(b)\). The symbol of the factor
remaining after \(U_0\) in the exact source has rate \(\Re R\).
All its factorial arguments remain regular, and the output product
obeys \(|Ke^{-2\pi iq}|<.7\) on the whole tube (11), as in
the typed-height theorem. Thus (10) may be multiplied by this
factor pointwise, with all outside scalars unchanged.

For the zero-height private coordinate the exact identity is
\[
                 \Psi_0(s,t)+R(t,p,q)
                   =\mathcal F_{\mathrm{cap}}(s,t,p,q).
\tag{12}
\]
The compact part of (10) therefore gives the original four-index
phase, with private height zero, on precisely its original real box.
The endpoint part gives the separate rate
\(37/50+\Re R\).

The residual phase has a useful height-reset inequality on (11):
\[
                      |\Im R_j|<2\pi,\qquad j=t,p,q.
\tag{13}
\]
For \(p,q\), the derivatives are exactly the \(p,q\) derivatives
in the already proved whole-rectangle gradient strips of
[the prepared critical-curve theorem](research_mixed_prepared_three_four_cap_critical_curve.md).
They require no outer stationarity and are independent of \(s\).
For \(t\),
\[
 R_t=g'(t+p)-g'(t)+2\pi ip.
\]
The original argument inequality for \(g'\) bounds its three
imaginary parts, divided by \(\pi\), in
\([-.84,.16]\), \([-.56,0]\), and \([.4,.84]\),
respectively. Their sum lies strictly in \((-1,1)\), which
proves the stronger \(|\Im R_t|<\pi\).

Hence
\[
 W_R(x,v)=\Re R(x+iv)-2\pi\sum_{j=t,p,q}|v_j|
\tag{14}
\]
does not increase when the absolute value of any height increases
with fixed sign. Resetting height coordinates to zero therefore
increases (14). The compact phase in (12) has the same reset
property by the original four-index gradient theorem.
The constant \(37/50\) is uniform and unaffected by this operation;
the sharper height-dependent (7) is not silently treated as constant.

## 4. All 26 outer horizontal aliases and the missing residuals

Apply the exact one-variable residue identity to the literal
three-index row. A horizontal tensor term has, in each coordinate,
height zero or the original lower or upper height in (11).
There are \(3^3-1=26\) terms other than the all-zero choice.
Its alias factors have exactly the debit
\(2\pi\sum|v_j|\), up to their uniformly bounded finite
denominators.

For the compact term of (10), keep one nonzero outer height and
reset the other heights in (12). Its containing rate is one of
the six original bounds \(B_{j,\pm}\), \(j=t,p,q\), in the
single face/alias record. Those six comparisons passed with gap
greater than \(1/20\), as recorded in
[the immutable attempt assessment](research_mixed_prepared_cap_face_alias_attempt.md).
Every source argument and every free real coordinate is the same
as in that record.

For the true-endpoint term define the six explicit residuals
\[
 D_{j,\pm}=\frac{37}{50}+
       \max_{x\in C_3}
       \{\Re R(x+i h_{j,\pm}e_j)
                          -2\pi|h_{j,\pm}|\},
                 \qquad j=t,p,q.
\tag{15}
\]
Equation (14) bounds every endpoint term among the 26 horizontal
aliases by one of (15). Thus their complete upper rate is
\[
       \max\left\{
             \max_{j=t,p,q;\,\pm}B_{j,\pm},
             \max_{j=t,p,q;\,\pm}D_{j,\pm}\right\}.
\tag{16}
\]
Every maximum in (15) is over a full independent real box.
The negative real Hessian of \(R\) is strictly positive on
the entire tube (11), by the pair argument in Section 2 of the
three-index main-sheet theorem, which uses only these height ranges.
Consequently each residual maximum has a valid global concave
support bound at any trial. No trial, value or sign of (15) has
been computed here.

The exact remaining condition for this horizontal-alias route is
\[
                         \max_{j,\pm}D_{j,\pm}<M,
             \qquad M=\Re\Phi_{\mathrm{cap}}(x_0,-2).
\tag{17}
\]
The already passed \(B_{j,\pm}\) do not imply (17), since no
uniform lower comparison between \(A_{\mathrm{real}}\) and
the true-endpoint ceiling has been proved.

## 5. Vertical currents and common-height joins remain distinct

The same argument controls the compact part of any outer vertical
lattice current by one of the six paid real \(t,p,q\) faces:
reset every height in (12), retaining the outer face. It also
identifies explicit sufficient endpoint bounds
\[
 E_{j,\pm}=\frac{37}{50}
     +\max_{\substack{x\in C_3\\x_j=x_{j,\pm}}}
                         \Re R(x),\qquad j=t,p,q.
\tag{18}
\]
Here \(x_{j,-}=L_j\) and \(x_{j,+}=R_j\) are the corresponding
lower and upper real endpoints of \(C_3\).
No sign of these six expressions is asserted. In particular the
physical-tail estimate for exact lattice nodes does not by itself
pay revived terms at the off-grid zero-height endpoints of a
vertical current.

The common-height joins of the zero-frequency three-index integral
have no alias penalty. They must be controlled separately, while
retaining the whole \(U_0\) dependence; (14) cannot be applied to
them after adding a penalty that their kernels do not possess.
The completed main-sheet and physical-tail theorem therefore remains
a partial source result. This reduction supplies exact source
identities and finite residual comparisons for a possible continuation,
not a completed prepared-cap asymptotic, whole outgoing-period
estimate, or knot-family theorem.
