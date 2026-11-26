# Boundary extension and vertical comparison for the second-selection half row

Research deduction, 6 November 2026. The main/right-half-row defect has
the same boundary-response cost as the completed main/main defect.
A direct vertical comparison also pays the central type-three reserve
under a stated smaller height condition. That condition is not asserted
for the entire reference domain. No root, primitive, sample, or parameter
cover is evaluated here.

## 1. The exact vertical change

Keep the original bare ordinary phase
\[
 Q_\beta(s;z,b)=g(s+z)+g(s+b)-(2+\beta)g(s)
                         -g(z)-g(b)+2\pi izs,
 \qquad g'(w)=\Log(1-e^{-2\pi iw}).
 \tag{1}
\]
Put \(H=1/100\), \(P=[11/50,9/20]\),
\(z=y+iH\), \(b=t+ik\), and let \(h=\Im v_*\) be
the original outgoing index height. The endpoint \(1/2+ih\)
belongs to its original main contour. For \(x\in P\), define
\[
 A_x(q)=\arctan\{\tanh(\pi q)\tan(\pi x)\}.
 \tag{2}
\]
The arctangent is the real principal one. Since \(\cos(\pi x)>0\),
factorization of \(1+e^{2\pi q-2\pi ix}\) gives its original
argument as \(-\pi x-A_x(q)\), with no logarithmic lift change.
Also \(g'(1/2+i\eta)=\log(1+e^{2\pi\eta})\) is real, so
\(\Re g(1/2+i\eta)=\Re g(1/2)=0\). Consequently the exact
vertical derivative is independent of the own flag:
\[
 \frac{d}{d\eta}\Re Q_\beta(1/2+i\eta;z,b)
       =\pi(t-y)+A_y(\eta+H)+A_t(\eta+k).
 \tag{3}
\]
Both original chirp contributions are included: its derivative is
\(-2\pi y\), which changes the two pair contributions
\(\pi(y+t)\) to \(\pi(t-y)\).

Thus the real half-row loss against this main endpoint is exactly
\[
 \begin{split}
 L(h,k;y,t)
 &:=\Re Q_\beta(1/2;z,b)-\Re Q_\beta(1/2+ih;z,b)\\
 &=-\pi(t-y)h-\int_0^h
             \{A_y(\eta+H)+A_t(\eta+k)\}\,d\eta.
 \end{split}
 \tag{4}
\]
Every outer allocation, Fourier alternative, and original affine
tangent is common to the two sides. Therefore any upper bound for
\(L\), uniform in \(y,t\), can be added to the main/main defect.
The main maximum may exceed its endpoint value, so (4) is a sufficient
comparison and is not an identity for the difference of the two maxima.

## 2. A sufficient small-height condition

**Proposition 1.** If
\[
             -3/250\le h\le0,\qquad k\le0,
 \tag{5}
\]
then for every \(y,t\in P\),
\[
                  L(h,k;y,t)<\frac{1693}{175000}<\frac1{100}.
 \tag{6}
\]
In particular, for first three flags \((1,1,0)\), wherever (5) holds, the
[completed type-three central gap](research_mixed_second_selected_central_completion.md)
greater than \(1/100\) implies a main/right-half-row gap greater
than \(57/175000\), for both complete Fourier alternatives.

*Proof.* Set \(r=-h\). On \([-r,0]\), the outgoing term
\(A_t(\eta+k)\) is nonpositive. The incoming term is nonpositive
for \(\eta\le-H\). For \(\eta+H\ge0\), use
\(\arctan q\le q\), \(\tanh q\le q\), and monotonicity of
\(\tan\) to obtain
\[
 \begin{split}
 L&\le \frac{23\pi}{100}r
   +\frac{\pi\tan(9\pi/20)}2
                   \{H^2-(H-r)_+^2\}\\
  &<\frac{23\pi}{100}r+10H^2
   \le\frac{1518}{175000}+\frac1{1000}
    =\frac{1693}{175000}.
 \end{split}
 \tag{7}
\]
Here \(\pi\tan(9\pi/20)=\pi\cot(\pi/20)<20\), since
\(\tan q>q\) for \(0<q<\pi/2\); the last inequality uses
\(\pi<22/7\) and \(r\le3/250\). Add (6) to the central
comparison at the admissible main endpoint, retaining all other target
coordinates and tangents. The difference
\(1/100-1693/175000=57/175000\) proves the consequence. \(\square\)

This proposition is a conditional analytic shortcut. The wider proved
own-three height rectangle \([-.065,.068]^2\) alone does not
establish (5). Indeed the particular independent heights
\[
       h=-3/50,\quad k=3/50,\quad y=11/50,\quad t=9/20
 \tag{8}
\]
give \(L>27\pi/2500>1/100\). To verify this without evaluating
the primitive, take \(\eta\in[-3/50,0]\). Then
\(A_t(\eta+k)\ge0\), while
\(A_y(\eta+H)>-\pi/20\), using \(y<1/4\) and
\(\eta+H\ge-1/20\). Equation (3) is therefore greater than
\(9\pi/50\); integrate it over an interval of length \(3/50\).
The values in (8) are not asserted to be a stationary reference, an
admissible prefix, or a word. They show only why the larger independent
height rectangle does not justify the endpoint comparison with loss
\(1/100\). They do not disprove main/half-row domination using a
different main trial.

## 3. The original reference phase and a constant formal coordinate

Use the original canonical prefix and allocated phase from the
[stationary-reference extension](research_mixed_stationary_reference_boundary_extension.md),
Section 2. In reference order \(r(c)=(a,u,z,v,b)\), write
\[
 F=Q_1(u;a,z)+Q_\beta(v;z,b)
            -\frac\alpha2g(a)-g(z)-\frac\beta2g(b).
 \tag{9}
\]
The original equations and boundary marginals are
\[
 F_u(r)=F_z(r)=F_v(r)=0,\qquad p_L=F_a(r),\quad p_R=F_b(r).
 \tag{10}
\]
In particular \(p_R\) contains the outgoing allocated halfweight
when \(\beta=1\). No reference index or tangent is replaced.

For \(\nu=1\) (factorial) or \(\nu=0\) (forced), introduce
the holomorphic five-variable function
\[
 \widehat\Psi_\nu(a,u,z,v,b)
   =F(a,u,z,1/2,b)+(1-\nu)g(z)+2\nu\pi iz.
 \tag{11}
\]
It is independent of its formal fourth coordinate \(v\).
Set
\[
 \begin{gathered}
 \Lambda_R=\operatorname{diag}(1,1,0,0,1),\qquad
 h_R=(0,0,H,0,0),\\
 x=(x_a,x_u,x_z,1/2,x_b),\qquad
 (x_a,x_u,x_z,x_b)\in P\times[.22,.5]\times P\times P,\\
 w=x+ih_R+\tfrac12\Lambda_R(r-\bar r).
 \end{gathered}
 \tag{12}
\]
Thus \(w_v=1/2\) is real and constant; the other three unselected
target heights are their original reference heights. Define
\[
 D_{R,\nu}(c;x)=\Re\{\widehat\Psi_\nu(w)-F(r)
                    -F'(r)\cdot(w-r)\}.
 \tag{13}
\]
By (10), its affine term is exactly
\(-p_L(w_a-a)-p_R(w_b-b)\). Formula (13) is the literal
main/right-half-row defect of the
[coupled half-row budget](research_mixed_second_selected_half_row_budget.md),
equations (4)--(6). It retains the reference \(g(v)\) term and
the original complex half-row constant; only their appropriate real
parts disappear when forming the rate.

## 4. The same response and extension loss

Assume a holomorphic canonical reference on a neighborhood of a closed
external rectangle or clipped disk, and the whole-image height
conditions (11) of the stationary-reference extension. All arguments
of the original primitive in (11)--(12) then have real part strictly
between zero and one. For example \(1/2+w_z\) and \(1/2+w_b\)
have real parts in \([.72,.95]\). No target branch cut is crossed.

Equation (17) of the coupled half-row budget gives the nonpositive
real Hessian on the four active variables \((a,u,z,b)\), for
both Fourier alternatives. The formal \(v\) row and column of
\(\widehat\Psi_\nu''\) vanish. Consequently
\(-\Re\widehat\Psi_\nu''\succeq0\) in the full five-dimensional
notation used in (13). This assertion uses the four-variable half-row
Hessian, not the main/main Hessian evaluated at a changed index height.

**Proposition 2.** With these hypotheses, for every fixed target in
(12),
\[
 \begin{split}
 \Delta_c D_{R,\nu}
 &=-\Re\{(\Lambda_Rr')^T
          \widehat\Psi_\nu''(w)\Lambda_R\bar r'\}
       +2\Re\{p_L'\overline{a'}+p_R'\overline{b'}\}\\
 &\ge-2\mathcal B(c),\qquad
 \mathcal B(c)=|p_L'(c)a'(c)|+|p_R'(c)b'(c)|.
 \end{split}
 \tag{14}
\]
The function \(\mathcal B\) is exactly the central response,
independent of the target and of the Fourier alternative. If
\(D_{R,\nu}\le-\gamma_R\) and \(\mathcal B\le B_0\)
on the entire boundary of a clipped disk of radius \(R_0\), then
\[
             \sup_x D_{R,\nu}\le-\gamma_R+B_0R_0^2/2
 \tag{15}
\]
throughout that clipped disk. On a rectangle of imaginary width
\(L\), the corresponding loss is \(B_0L^2/4\).

*Proof.* Apply the exact Laplacian identity to (13), using (10).
The only nonzero marginal derivatives are the original boundary
ones, and both corresponding entries of \(\Lambda_R\) equal one.
The Hessian observation proves the sign of the first term. Each term
in \(\mathcal B\) is the modulus of a holomorphic function, so
the same subharmonic response and disk or rectangle barrier proof
applies, separately for every fixed target. Take the target supremum
only afterwards. \(\square\)

The original left index interval starts at \(.125\). Its positive
gradient barrier at \(.22\) is unchanged by replacing the right
index by \(1/2\), as proved in Section 3 of the coupled half-row
budget. Thus restricting to (12) preserves the original maximum.
For the actual external domains \(K_3,K_4\), the respective losses
in (15) are
\[
       \frac{6889}{2000000}B_0,\qquad \frac9{5000}B_0.
 \tag{16}
\]
Every circular arc and clipping segment remains part of the required
boundary. A previously certified bound for the original response on
these same references can therefore be reused unchanged; it does not
provide the new boundary half-row gap itself.

In particular, the right side of equation (28) of the coupled half-row
budget may supply \(-\gamma_R\) on those boundaries, using its
same-reference trial value and three gains. Both Fourier alternatives,
the original reference action, and both boundary tangents remain
explicit. The two uniform boundary scalar signs are the remaining
input to this route. No full finite-source or whole-chain bound is
claimed here.

For \(\alpha=1,\beta=0\), the completed central theorem already
establishes the required whole-image heights and the response bounds
\(B_0<329/200\) on \(K_3\) and \(B_0<411/200\) on \(K_4\).
They are statements about the original reference curve, so no new
response or reference calculation is needed for (14). Their half-row
extension costs are strictly below
\[
       L_3=\frac{2266481}{400000000},\qquad
       L_4=\frac{3699}{1000000}.
 \tag{17}
\]
Accordingly, it suffices to bound both half-row scalar majorants (28)
on every boundary arc and segment by the following respective upper
bounds:
\[
  -\frac{2391481}{400000000}\quad(K_3),\qquad
  -\frac{8023}{2000000}\quad(K_4).
 \tag{18}
\]
These numbers are exactly \(-L_j-1/3200\). If (18) holds, the
entire canonical type-three half-row comparison has gap greater than
\(1/3200\), uniformly in the four real targets and on both external
domains. The inequalities (18) are not proved in this note.
