# The marked cusp boundary and the protected cut residue

Private written proof, 17 November 2026. No mathematical program,
numerical test, or public/frozen edit is used.

The classical determinant coordinates associated locally with the two
protected faces reach a boundary of the actual marked framing chart.
Their local geometry is not the intersection
obtained by varying two independent projective auxiliary flags.
The marked eigenvector constrains those flags. We compute the resulting
divisor, its successive blow-ups, and the precise difference between
the protected logarithmic form and the geometric framing form.
This identifies a singular Jacobian and a relative section current;
it does not compute a selected geometric coefficient.

## 1. The finite protected residue and its centering units

Use the original connected homogeneous face source of [H], with
\(N\geq3\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
There are \(R\) boxes, two protected faces \(u,v\), and \(R\)
ordinary faces. Its full numerator
\[
 \mathcal P_N(L;\boldsymbol\sigma)=\prod_e H_{f_e}(L)
 \tag{1}
\]
is homogeneous of degree \(dR\), with nonnegative face exponents.
The coupons are the original full Casimir polynomials, including
their repeated-node data, signed crossing factors, and any retained
external parameters \(\boldsymbol\sigma\). The exact marked scalar is
the coefficient with ordinary exponents \(d\) and protected exponents
zero. All external scalar lines remain as in [H].

Choose an ordinary face \(w\) as homogeneous coordinate and set
\(L_w=1\). Homogeneity recovers its missing exponent \(d\).
Writing \(z\) for the other ordinary variables, the protected part
of the exact coefficient operation is therefore
\[
 \underset{L_u=L_v=0}{\operatorname{Res}}\,
 \mathcal P_N(L_u,L_v,z,1;\boldsymbol\sigma)
                  d\log L_u\wedge d\log L_v
       =\mathcal P_N(0,0,z,1;\boldsymbol\sigma).
 \tag{2}
\]
The remaining ordinary coefficient extractions are still required.
This is a double coefficient residue, not evaluation at a regular
nonzero framing coordinate. Every external parameter derivative
commutes with (2). In particular no original Casimir normal is
discarded by writing this identity.

Here is the precise local comparison with determinant coordinates.
For the literal face quartet \((x,b,c,y)\), [H, (4)--(7a)] gives
\[
 Q^{a}=-q^{-1}x/b,\quad Q^{b_0}=-q^{-1}b/y,
 \qquad Q^{a'}=-q^{-1}x/c,\quad Q^{b'}=-q^{-1}c/y.
 \tag{3}
\]
The symbols \(b\) and \(b_0\) in (3) respectively denote a face
variable and a head index. On the classical regular crossing chart
of [F], let \(w_f=\det(p,s_f)\). Its positive-crossing ratios are
\(A=w_0/w_M\), \(B=w_M/w_R\), and
\(C=w_0w_R/(w_Mw_P)\). The exact unit change
\[
 (x,b,c,y)=(Qw_0,-q w_M,-q w_P,w_R)
 \tag{4}
\]
turns (3) into those input and output ratios. For example
\(-q^{-1}x/b=w_0/w_M\), and the transfer cross-ratio is unchanged.
The inverse crossing uses the same four-clock adapter with its
actual reversed input/output roles. It does not change the finite
endpoint or Cartan factors in [H].

The local units in (4) can equivalently be written
\[
 L_f=\gamma_f R_f,\qquad \gamma_f=q^{-d\nu_f},\qquad
 (\nu_W,\nu_S,\nu_N,\nu_E)=(2,1,1,0).
 \tag{5}
\]
Here the local \(R\)-ratios are the determinant ratios of [F].
This is not a proof that one winding \(\nu\) gives this quartet
simultaneously at every original flat-plat box. At a reversed strand
the actual dual head is \(i^\vee=d-i\), so its clock is
\(Q^{i^\vee}=Q^dQ^{-i}\); only the centered head changes sign.
A conserved knot-oriented winding therefore has signed differences
in an upward physical box chart. The affine dual factors at bends
must still be transported to prove a global Morse-source determinant
adapter. No such global adapter is asserted here.

For any prescribed fixed units \(\gamma_f\) on the actual finite
face variables, the coefficient change is exactly
\[
 [L^{\mathbf n}]\mathcal P_N(L)
 =\Bigl(\prod_f\gamma_f^{-n_f}\Bigr)
       [R^{\mathbf n}]\mathcal P_N(\gamma R).
 \tag{6}
\]
Here \(n_u=n_v=0\) and \(n_f=d\) on ordinary faces.
The protected logarithmic forms are unchanged by constant units.
Equation (6) does not construct a globally compatible determinant
choice of those units. In the following classical calculation we
use the dephased determinant ratios calibrated by (4), so that the
diagonal direction is literally ratio one. Comparing this entire
marked framing family with the finite flat-plat source still requires
the global dual/frame adapter as well as the relative pushforward.

## 2. The marked columns, not two independent flags

In [B, (5.4)] the actual constant boundary vector selects the
meridian eigenline \((1,1)^t\). The auxiliary basis vectors in [F]
are \(s=e_1\), \(p=e_2\); consequently their sum is the selected
eigenvector. Fix a complete reference meridian and its selected vector:
\[
 \mu=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad e_1.
\]
A normalized actual marked frame is
\[
 F(r,h)=\begin{pmatrix}r&1-r\\h&-h\end{pmatrix},\quad h\ne0,
 \qquad S=F e_1=(r,h)^t,\quad P=F e_2=(1-r,-h)^t.
 \tag{7}
\]
Thus \(P+S=e_1\), and \(\det F=-h\). Every projective frame
sending the selected line to \(e_1\) has this normalization locally.
The physical cut meridian is, directly,
\[
 F^{-1}\mu F=\begin{pmatrix}1+h&-h\\h&1-h\end{pmatrix},
 \qquad A=(1+h)^{-1}.
 \tag{8}
\]
For the two adjacent regions, read in the chosen meridian direction,
\[
 w_u=\det(P,S)=h,\qquad
 w_v=\det(P,\mu S)=h(1+h).
 \tag{9}
\]
Their common zero in this marked surface is the divisor \(h=0\).
It is not a length-two complete intersection. Reversing the local
meridian direction replaces \(\mu\) by its inverse and reverses
the corresponding signed formulas; we keep the direction in (9).

In particular, one cannot normalize both auxiliary first coordinates
to one independently and then keep their scale product a unit at this
boundary. Such independent projective normalizations forget the
marked vector relation in (7). No residue formula based on that
different two-flag center is used here.

## 3. An ordinary anchor and the second blow-up

Let an ordinary region have reference transport
\(g=\left(\begin{smallmatrix}a&b\\c&d_0\end{smallmatrix}\right)\).
Its determinant is exactly
\[
 W(r,h)=\det(P,gS)
   =c r(1-r)+h\{d_0+(a-d_0)r\}+b h^2.
 \tag{10}
\]
Work near \(h=0,r=r_0\), where \(W(r_0,0)\ne0\), and use this
ordinary face as homogeneous anchor. Thus \(c\ne0\) and
\(r_0\notin\{0,1\}\). The calculation is local to any such
anchor; it does not assert that every chosen ordinary face works.
For an irreducible complete crossing chart with all diagram regions
retained, some ordinary region has \(c\ne0\): otherwise all its
region words would preserve the selected line, and adjacent-region
transport would make every meridian preserve it. The two regions
in (9) themselves have \(c=0\).

In the local classical comparison, the normalized protected determinant
coordinates are
\[
 x=h/W(r,h),\qquad y=x(1+h).
 \tag{11}
\]
The first blow-up coordinate \(T=y/x\) therefore tends to one.
Blow up the point \(x=0,T=1\) once more, using
\[
 v=(T-1)/x=(y-x)/x^2.
\]
On the marked surface this gives the exact equations
\[
 v=W(r,h),\qquad h=xv,\qquad
 v=W(r,xv),\qquad v\big|_{x=0}=c r(1-r).
 \tag{12}
\]
If additionally \(r_0\ne1/2\), then
\(W_r(r_0,0)=c(1-2r_0)\ne0\). The implicit function theorem
solves \(r\) holomorphically in \((x,v)\). These are genuine
local boundary coordinates on each such branch. Globally over
the exceptional \(v\)-line, the equation \(v=c r(1-r)\) has
two branches and a branch point at \(r=1/2\); they are not
identified. The anchor also fails at \(r=0,1\).

All other region determinants vary in this calculation. For any
reference word \(g_f\), they have the same polynomial form (10),
and their normalized coordinates are \(W_f(r,h)/W(r,h)\).
They have not been held artificially independent while restricting
to the critical framing surface. In particular this two-dimensional
restriction is not a full off-critical coordinate substitution in
the remaining physical-flow period.

## 4. The meridian normal retains the collapsed parameter

Keep the selected eigenvalue \(M^{-1}\) explicit by using the regular
classical reference family
\[
 \mu_M=\begin{pmatrix}M^{-1}&1\\0&M\end{pmatrix}
\]
with the same columns (7). Direct determinants give
\[
 \det(P,\mu_M S)
  =h\{M+(M^{-1}-M)r+h\},\qquad
 \frac yx=M+(M^{-1}-M)r+h.
 \tag{13}
\]
Any common ordinary anchor cancels from the ratio. Hence, at fixed
\(r,h\),
\[
 \left.(M\partial_M)(y/x)\right|_{M=1}=1-2r.
 \tag{14}
\]
The framing parameter forgotten by the complete first blow-up is
visible in this normal family, as well as in (12). This is a
classical marked matrix identity on a specified family. It is not
a generic-q pivotal identity, nor an identification of a fixed-root
quantum normal with differentiation of these reference matrices.
No original scalar is replaced by an inserted normal observable.

## 5. The two forms and their different boundary behavior

The protected residue form has an elementary pullback. From (11),
\[
 d\log x\wedge d\log y
 =-\frac{W_r}{W(1+h)}\,dr\wedge dh
 =\frac{dx\wedge dv}{1+xv}.
 \tag{15}
\]
It is holomorphic at a finite \(v\) point of the second exceptional
divisor. Thus a bounded holomorphic coefficient multiplying this
two-form has no local logarithmic residue there. This statement
concerns the displayed two-form, not the result of transverse
Gaussian contraction of the full source.

The actual complete framing form in [R] and [C] is instead
\[
 \Omega_{\rm cut}=-\frac{dr\wedge dh}{h(1+h)}.
\]
Using (12) gives
\[
 \Omega_{\rm cut}
  =\frac{dx\wedge dv}{xW_r(r,xv)(1+xv)}
  =\frac1{xW_r}\,d\log x\wedge d\log y.
 \tag{16}
\]
The multiplier has a genuine simple pole. It is not an invertible
bounded holomorphic gauge factor. With residue convention
\(\operatorname{Res}_{x=0}((dx/x)\wedge\eta)=\eta|_{x=0}\),
\[
 \operatorname{Res}_{x=0}\Omega_{\rm cut}
       =\frac{dv}{c(1-2r)}=dr.
 \tag{17}
\]
This is an exact additive one-form on each regular exceptional
\(r\)-chart, not a prescribed nonzero period on a closed cycle.

The principal transverse Gaussian comparison recorded in [C] gives
\(\Omega_{\beta,0}=c_\beta\Omega_{\rm cut}\), with its nonzero
marked half-density and base lines retained. At fixed character
\(c_\beta\) is constant along the framing orbit. Its residue is
therefore \(c_\beta dr\). Equations (15)--(17) specify the singular
factor a comparison with the protected residue must accommodate.
They do not prove that taking this Gaussian first commutes with
the original residue, determine higher Gaussian poles, or identify
the original selected chain with the exceptional divisor.

## 6. The specified relative interval does not enter this collar

Set \(t=r/h\). The original classical relative model [R] has
\[
 \Omega_{\rm cut}=dt\wedge d\log A,
 \qquad A=(1+h)^{-1},
 \tag{18}
\]
and meridian translation \(t\mapsto t+1\). Its normalized
relative endpoints are \(t=0,1\). For bounded \(t\), substitute
\(r=ht\) in (10):
\[
 W(ht,h)=h(ct+d_0)+O(h^2),\qquad
 x\longrightarrow\frac1{ct+d_0}
 \tag{19}
\]
uniformly on compact \(t\)-sets on which \(ct+d_0\ne0\).
Thus this bounded relative interval does not approach \(x=y=0\)
in the anchored chart. The collar in (12) instead has
\(r\to r_0\notin\{0,1\}\), so \(t=r/h\) escapes.
Zeros of \(ct+d_0\) require an additional anchor chart and are
not discarded by (19).

The singular section change needed to shift the interval toward
\(r=r_*\ne0,1\) is explicit:
\[
 t_0(A)=r_*/h=\frac{r_*A}{1-A}.
\]
Although translating \(t\) by \(t_0(A)\) preserves the interior
two-form (18), it changes its primitive \(t\,d\log A\) by
\[
 t_0(A)d\log A=\frac{r_*\,dA}{1-A}
                 =-r_*d\log(1-A).
 \tag{20}
\]
Its residue at \(A=1\) is \(-r_*\). Both endpoint co-sources
must be transported with it. This nonzero current does not imply
that the correctly completed relative period changes: the two
endpoint contributions may cancel after the actual comparison.
It does show why the regular-section invariance argument cannot
delete the added boundary term.

There is exact finite source data at this same root. In [R],
\[
 C_N=\mathbb C[A,A^{-1}]/(A^N-1),\quad
 \phi_N(f)=N^{-1}\sum_{a=0}^{N-1}f(Q^a),\quad
 \omega_N=N^{-1}d\log(A^N-1).
 \tag{21}
\]
The root idempotent
\(\epsilon_1=N^{-1}\sum_{j=0}^{N-1}A^j\) is killed by
localizing at \(A-1\), but \(\phi_N(\epsilon_1)=1/N\).
The bare co-source consequently does not descend through that
localization. The Ward-localized repair in [R] changes its
representative with explicit homotopy and excursion terms;
it is not permission to remove (20) without their transport.

The whole normal family likewise retains \(A^N=U\), the
\((U-1)\)-residue, and the distinction between literal and
reduced pivot lifts. Those data are not replaced by evaluating
\(A^N=1\) before a normal derivative. The finite identities
(1)--(6) retain all coupon normals, but they do not identify
these quantum normal co-sources with the classical family (13).

Finally [R] distinguishes its finite boundary resolution's auxiliary
\(t\) from the internal zero mode \(r/h\) produced by geometric
Gaussian reduction: their source-preserving comparison remains to
be proved. Accordingly (19)--(20) compare the specified classical
relative model and candidate sections; they do not describe a
previously established motion of the original selected cycle.

## 7. What the calculation settles

The actual marked boundary is a divisor with a diagonal first
blow-up direction, followed by the explicit second blow-up (12).
Its protected logarithmic form is regular there, whereas the
known principal framing form has the pole (16). Reaching that
collar from a bounded meridian-relative section introduces the
retained current (20) at a root seen by the finite co-source.
These are exact boundary calculations. They do not imply a
vanishing geometric coefficient, a nonzero one, a global period
identity, or a volume asymptotic. No independent-flags shortcut,
new quantum operator, global Morse-source determinant adapter, or
replacement of the averaged marked cut is used.

## Complete direct written sources

All five complete texts and their directly used implications were read.

| Label | Source | SHA-256 |
|---|---|---|
| H | [Homogeneous full face source](actual_homogeneous_casimir_face_source.md) | a7d89f310f2cb4193ab73ef49f715198b224d1c3756d84c4cb940d7fa850c2f2 |
| B | [Actual marked braid chart](marked_braid_holonomy.md) | eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f |
| F | [Actual crossing fundamental cycle](crossing_fundamental_cycle.md) | 0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f |
| R | [Relative framing and literal cut](relative_framing_source_transgression.md) | 1c27a6559bf59f74d8fec44e7b6dd076ec1a06445fcb1bc93ca98b5838ae4cc8 |
| C | [Compact framing and boundary residue](compact_framing_gauge_and_boundary_residue.md) | 72ecf6d9733b5588e01e843c20d0208f0cd6542b1cbc8d69dbe61d8bfd0c4867 |
