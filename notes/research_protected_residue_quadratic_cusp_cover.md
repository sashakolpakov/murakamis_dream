# The protected residue on the quadratic cusp cover

The marked cusp surface has two different boundaries above the two
protected face coordinates. The finite-frame boundary approaches the
diagonal direction and has no protected logarithmic residue. The
infinite-frame boundary carries the whole double residue, with
multiplicity two. This note computes that multiplicity and the exact
transported amplitude of the full finite coefficient source.

The change of variables used for the coefficient identity keeps all
ordinary face variables independent. Restriction to the geometric
critical surface, where those variables also vary, is a different
operation. No identification of its selected relative chain is made.

## 1. The complete coefficient source

Use the homogeneous marked face source [H], with \(N\geq3\),
\(d=N-1\), two protected faces, and \(R\) ordinary faces. Set one
ordinary face equal to one, and denote the other ordinary variables by
\(\zeta=(\zeta_1,\ldots,\zeta_{R-1})\). The exact coefficient is
\[
 Z_N=\operatorname{CT}_{\zeta}\!
       \left[\mathcal P_N(0,0,\zeta,1)
                       \prod_{\ell=1}^{R-1}\zeta_\ell^{-d}\right].
 \tag{1}
\]
Here \(\mathcal P_N(x,y,\zeta,1)\) is the entire original numerator:
all Casimir coupons, their repeated-node data, crossing factors, and
external parameters are retained. The external scalar normalization
is the one in [H]. Write
\[
 \Xi(\zeta)=\prod_\ell\zeta_\ell^{-d}\,
                  d\log\zeta_1\wedge\cdots\wedge d\log\zeta_{R-1}.
 \tag{2}
\]
Thus (1) is the iterated residue of
\(\mathcal P_N\,d\log x\wedge d\log y\wedge\Xi\).
Fixed centering units are handled by the exact coefficient change
[B, (6)]; they do not change the protected logarithmic form.
The local determinant calibration of [B] is not a global
Morse-source determinant adapter.

Fix \(g=\left(\begin{smallmatrix}a&b\\c&d_0\end{smallmatrix}\right)\)
with determinant one and \(c\ne0\), and put
\[
 \begin{split}
 B(h)&=c+(a-d_0)h,\\
 W(r,h)&=-cr^2+B(h)r+d_0h+bh^2,\\
 x&=h/W(r,h),\qquad y=x(1+h).
 \end{split}
 \tag{3}
\]
These are exactly the marked determinant formulas in [B]. For the
finite coefficient identity, (3) is an algebraic change of the two
protected variables; denote its extension by the identity on
\(\zeta\) by \(F\).
Constant \(g\) is always permitted for this algebraic operation.

More generally the entries of \(g\) may depend holomorphically on
\(\zeta\) in a neighborhood of the chosen ordinary coefficient torus,
provided \(c\) is a unit there. All constructions below are then
uniform over that compact torus. This hypothesis is not asserted
for an arbitrary determinant anchor on the original geometric cycle.
All two-form identities below are vertical, with \(\zeta\) fixed.
Wedging with \(\Xi\) gives the exact full-form identities even
when these coefficients depend on \(\zeta\).

## 2. The infinity chart and its complete coefficient cycle

Compactify the \(r\)-line and use \(z=1/r\). Then
\[
 \begin{split}
 \widehat W(z,h)&=z^2W(1/z,h)\\
  &=-c+B(h)z+(d_0h+bh^2)z^2,\\
 x&=hz^2/\widehat W,\qquad y=x(1+h).
 \end{split}
 \tag{4}
\]
Put \(k=1+h=y/x\). Near \((z,k)=(0,0)\), both \(h\) and
\(\widehat W\) are units, and
\[
 x=z^2 u(z,k),\qquad y=z^2 k u(z,k),
 \qquad u=h/\widehat W\ne0.
 \tag{5}
\]
This is a degree-two map to the first blow-up chart \((x,k)\)
of the protected origin, followed by its blow-down \((x,k)\mapsto
(x,xk)\). It is not asserted to be finite over the blown-down origin.

Choose \(0<\delta<1/2\) and then sufficiently small \(\rho>0\).
On the closed polydisc \(|z|\leq\rho,\ |k|\leq\delta\),
\(\widehat W\) has no zero. Give the torus
\[
 \mathcal T_{\rho,\delta}=\{|z|=\rho,\ |k|=\delta\}
 \tag{6}
\]
the order \(z,k\). On each spectator fiber the winding matrix of its
image in the \(x,y\) torus is
\[
 \begin{pmatrix}2&0\\2&1\end{pmatrix}.
 \tag{7}
\]
Indeed the unit \(u\) has a holomorphic logarithm on this polydisc,
so contributes no winding in either circle. The image of (6)
therefore has twice the oriented protected torus class. Equivalently,
the full inverse image of a sufficiently small torus
\(|x|=\epsilon,\ |k|=\delta\) is an unramified two-fold cover of
that torus. Choosing a single sheet after one \(x\)-turn is invalid:
the two roots are exchanged.

Let \(\beta=d\log x\wedge d\log y\). Direct differentiation gives
\[
 F^*\beta=
 \left(\frac2z-\frac{\widehat W_z}{\widehat W}\right)
                         \frac{dz\wedge dh}{1+h}.
 \tag{8}
\]
When the entries of \(g\) depend on \(\zeta\), (8) denotes the
vertical part of the pullback. Every omitted term contains a
\(d\zeta_\ell\) and vanishes after wedging with \(\Xi\).

Since \(x,y\) vanish at \(z=0\), for the full numerator one obtains
\[
 \operatorname{Res}_{h=-1}\operatorname{Res}_{z=0}
 \left[\mathcal P_N(x(z,h),y(z,h),\zeta,1)\,F^*\beta\right]
       =2\,\mathcal P_N(0,0,\zeta,1).
 \tag{9}
\]
Our order convention first extracts \(dz/z\), then \(dh/(1+h)\).
Consequently the exact original coefficient is
\[
 Z_N=
 \frac{1}{2(2\pi i)^{R+1}}
 \int_{\Gamma_\zeta}\int_{\mathcal T_{\rho,\delta}}
 \mathcal P_N(x(z,h),y(z,h),\zeta,1)\,
                 F^*\beta\wedge\Xi.
 \tag{10}
\]
Here \(\Gamma_\zeta\) is any ordinary coefficient torus on which
the preceding unit condition holds. Formula (9), or Cauchy's
theorem on each fiber, proves (10) without a choice of a sheet.
All original external parameter derivatives commute with this
identity on buffered parameter neighborhoods. The dependence of
the map on those parameters must also be differentiated.
This concerns parameter families for which the original fixed-root
coefficient identity holds; it supplies no new genuine-q extension.

## 3. The finite boundary and the transported odd amplitude

The finite-\(r\) boundary in [B] has \(h=0\), with
\(W(r,0)=cr(1-r)\ne0\). Its first blow-up direction is \(k=1\).
The second blow-up coordinate is
\[
 v=(y-x)/x^2,\qquad h=xv,\qquad v=W(r,xv).
 \tag{11}
\]
At a point with \(r\notin\{0,1,1/2\}\), this is a regular chart
and \(v|_{x=0}=cr(1-r)\). In it,
\[
 \beta=\frac{dx\wedge dv}{1+xv}.
 \tag{12}
\]
Thus a bounded holomorphic coefficient has no protected logarithmic
residue on this finite second exceptional chart. This is consistent
with (9): the torus there is at the distinct first exceptional
direction \(k=0\), on the infinite-\(r\) chart.

Put \(D=W_r=B(h)-2cr\). The complete framing form of [B, R] obeys
\[
 \Omega_{\rm cut}=-\frac{dr\wedge dh}{h(1+h)}
     =\frac{\beta}{xD},\qquad
 \mathcal P_N\,\beta=(xD\,\mathcal P_N)\Omega_{\rm cut}.
 \tag{13}
\]
The last equality transports the entire coefficient amplitude,
not merely its value at a selected character. In the finite chart,
\(xD\) has a simple zero in \(x\), canceling the framing pole.
At infinity,
\[
 \Omega_{\rm cut}=\frac{dz\wedge dh}{z^2h(1+h)},\qquad
 xD=2hz+O(z^2).
 \tag{14}
\]
The transported amplitude cancels exactly one order of the framing
double pole, producing the logarithmic residue (8). The residue
of \(\Omega_{\rm cut}\) itself along \(z=0\) is zero.

The deck involution and its scalar trace are also explicit:
\[
 \iota(r,h)=(B(h)/c-r,h),\qquad
 W\circ\iota=W,\quad D\circ\iota=-D,\quad
 \iota^*\Omega_{\rm cut}=-\Omega_{\rm cut}.
 \tag{15}
\]
At \(h=0\) it is \(r\mapsto1-r\); at infinity its expression is
\(z\mapsto z/((B/c)z-1)\), with derivative \(-1\) at \(z=0\).
The quadratic extension is described by
\[
 D^2=B(h)^2+4c\{d_0h+bh^2-h/x\},\qquad h=y/x-1.
 \tag{16}
\]
For any meromorphic scalar amplitude \(a=a_0+a_1D\) over the
base field, summing its two differential-form branches gives
\[
 \operatorname{Tr}(a\Omega_{\rm cut})=\frac{2a_1}{x}\,\beta.
 \tag{17}
\]
The identity extends meromorphically across the branch divisor.
In particular a character-constant coefficient \(c_\beta\), with
the identity lift on its retained coefficient line, has zero
trace when multiplying \(\Omega_{\rm cut}\). A different lift of
a sign line or a different selected chain is not this scalar trace.
Higher coefficients can have a nonzero odd part even when this
principal trace vanishes.

For the full coefficient source in (13), however,
\(a=xD\,\mathcal P_N\) has \(a_1=x\mathcal P_N\). Hence
\[
 \operatorname{Tr}\bigl((xD\,\mathcal P_N)\Omega_{\rm cut}\bigr)
                  =2\mathcal P_N\,\beta.
 \tag{18}
\]
Equations (9), (14), and (18) give the same degree-two
normalization. Replacing the amplitude \(xD\,\mathcal P_N\)
by a character-constant Gaussian coefficient would change it.

## 4. The remaining poles and the relative endpoints

The infinity residue of (8) is the global rational one-form
\[
 \operatorname{Res}_{z=0}F^*\beta
       =2\,\frac{dh}{1+h}=-2\,d\log A,
       \qquad A=(1+h)^{-1}.
 \tag{19}
\]
On the compact \(h\)-line its residues are \(+2\) at \(h=-1\)
and \(-2\) at \(h=\infty\), corresponding to \(A=\infty\)
and \(A=0\). There is no pole at \(h=0\), or \(A=1\).
The two poles cannot be discarded when changing the remaining
one-dimensional cycle. Likewise the generic two zeros of \(W\)
carry the other \(r\)-fiber residues of \(\beta\), each
\(-dh/(1+h)\); they lie outside (6). The full numerator can
introduce higher poles there. Formula (10) does not cross them.

The classical relative coordinate in [R] is \(t=r/h\), with
specified endpoints \(t=0,1\), and
\[
 \Omega_{\rm cut}=dt\wedge d\log A,\qquad
 t\,d\log A=-\frac{dh}{zh(1+h)}.
 \tag{20}
\]
For \(h\) near \(-1\), the endpoint sections \(r=0\) and
\(r=h\) are finite and do not approach the corner
\((r,h)=(\infty,-1)\). The primitive in (20) has a pole
there even though the \(z\)-residue of its derivative is zero.
Thus the cover cycle (6) is not obtained by silently extending
or identifying those endpoint sections.

For a section translation \(t\mapsto t+t_0(A)\), [R] retains
the boundary primitive \(t_0(A)d\log A\). Polar sections require
their additional currents. The finite cut instead uses
\[
 \omega_N=\frac1N d\log(A^N-1),\qquad
 \phi_N(f)=\frac1N\sum_{a=0}^{N-1}f(Q^a).
 \tag{21}
\]
It is not the one-form in (19). Its canonical-residue comparison
retains the chosen degree-\(<N\) lift, the \(A^N\) carry, and
all endpoint co-sources. In particular the \(A=1\) idempotent
has \(\phi_N=1/N\), although (19) is regular there.
No replacement of (21) by (19) is used in (10).

Finally, in the actual critical framing family the other normalized
face coordinates are \(W_f(r,h)/W(r,h)\). Their limits at
finite \(h,r=\infty\) are \(c_f/c\), and they are not the
independent \(\zeta\)'s in (10). Pulling the full coefficient form
back to that two-dimensional critical surface is not an invertible
change of all its variables. The exact full-source cover identity
therefore supplies neither the global Morse/determinant adapter
nor the transverse pushforward and relative-chain comparison.
It computes the protected residue and its amplitude without deciding
the selected geometric coefficient.

## Direct sources

| Label | Source | SHA-256 |
|---|---|---|
| H | [Homogeneous full face source](actual_homogeneous_casimir_face_source.md) | a7d89f310f2cb4193ab73ef49f715198b224d1c3756d84c4cb940d7fa850c2f2 |
| B | [Marked cusp boundary and cut residue](research_marked_cusp_boundary_and_cut_residue.md) | 7bfe3bf0ae6fe563aa32ab232bcafe66d36443415dd9ec68933b069e131e942a |
| R | [Relative framing source transgression](relative_framing_source_transgression.md) | 1c27a6559bf59f74d8fec44e7b6dd076ec1a06445fcb1bc93ca98b5838ae4cc8 |
