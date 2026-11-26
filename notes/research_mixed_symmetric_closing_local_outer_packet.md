# The actual local outer contribution for symmetric 343

Private finite-source deduction, 9 November 2026. The complete
inner-three packet now reaches the actual middle angle of the
positive symmetric \(343\) solution. The original geometric
Hessian supplies strict horizontal quadratic decrease after the
two end angles are eliminated. Consequently a specified local
piece of the exact outer Hermite contour has a nonzero Gaussian
asymptotic, including two independent ordinary boundary colors.

The rest of the outer contour is retained explicitly below.
This note does not estimate that remainder or assert a complete
closing asymptotic. No mathematical numerical evaluation, saved
arithmetic, import, compilation, or frozen-source edit is used.

## 1. Exact closing and its geometric point

Keep the original definitions
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad
C_{N,n}=q^{nD^2/4},\\
\mathcal A_N=\mathbb C[x]/(2T_N(x/2)+2),\qquad
\phi_N(f)=\eta_NN^2[x^D]\operatorname{rem}_{2T_N(x/2)+2}f,\\
c_a=2\cos((2a+1)\pi/N),\qquad
S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\\
K_N(w,x)=\sum_{j=0}^D e_j(w)e_j(x),\qquad
\mathscr Q_N(w,u)=
\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N(-2\cos u,x)] .
\end{gathered}                                                     \tag{1}
\]
The exact [symmetric contraction](research_mixed_symmetric_343_closing_trace_and_domain.md),
equation (4), is
\[
Z_{343,N}(w_L,w_R)
 =\phi_N^{(z)}[R_N(z)^4Q_N(w_L,z)Q_N(w_R,z)],
\qquad Q_N(w,-2\cos u)=\mathscr Q_N(w,u).
                                                                    \tag{2}
\]
It is an ordinary polynomial identity in both free colors. Only
the variable under \(\phi_N\) is reduced. Its full double-root
normals and odd simple node have not been replaced by values.

The positive unit-charge geometric solution has equal end angles
\(t_g\) and middle angle \(u_g=\beta_g-iK_g\). The original returns
obey
\[
\begin{split}
\operatorname{arsinh}\tan(t_g/2)
 +\operatorname{arsinh}\{\cos(u_g/2)\tan(t_g/2)\}
 &=i(3t_g/2-\pi),\\
\operatorname{arsinh}\{\cos(t_g/2)\tan(u_g/2)\}
 &=i(u_g-\pi/2).
\end{split}                                                       \tag{3}
\]
The [angle-box theorem](research_mixed_symmetric_closing_angle_and_height_box.md)
and [height localization](research_mixed_symmetric_closing_height_below_seven_tenths.md)
prove, on this same unsquared logarithmic sheet,
\[
0<\beta_g<\pi/2,\qquad 17/30<K_g<7/10 .
                                                                    \tag{4}
\]
Their cubic comparison also identifies \(t_g=t_0(u_g)\), the
selected end root in the
[complete inner theorem](research_mixed_symmetric_closing_complete_inner_asymptotic.md).
Thus \(u_g\) lies strictly inside its independent outgoing rectangle
\[
\mathcal V_+=\{\beta-iK:0\le\beta\le\pi/2,\ 0\le K\le7/10\}.
                                                                    \tag{5}
\]

Use the [ordinary incoming-neighborhood theorem](research_mixed_symmetric_closing_incoming_neighborhood.md)
in its original normalization:
\[
\mathscr Q_N(w,u)
 =C_{N,3}N^{-3/2}A(w,u)e^{NS(w,u)}
                     (1+E_N(w,u)),\qquad E_N=O(N^{-1}).
                                                                    \tag{6}
\]
Here \(S,A\) are holomorphic on a neighborhood of an incoming
disk about \(-2\) times (5), \(A\ne0\), and all fixed normalized
mixed derivatives are \(O(N^{-1})\) on outgoing interior compacts.
At \(w=-2\),
\[
S(-2,u)=\Phi_0(t_0(u),u),\qquad
\Phi_0(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it .
                                                                    \tag{7}
\]
Both full edges occur in (6); no trace-only shortening is being
substituted for an off-grid full function.

## 2. The outer Hessian is strictly negative in real part

At complete outside angles consider the original three-angle
action, before eliminating either end:
\[
\begin{split}
\mathcal H(t_L,t_R,u)
={}&\psi(0,t_L)+\psi(t_L,u)+\psi(u,t_R)+\psi(t_R,0)\\
&+\frac{i}{4\pi}(3t_L^2+3t_R^2+4u^2)-i(t_L+t_R+u).
\end{split}                                                       \tag{8}
\]
Its gradient vanishes at \((t_g,t_g,u_g)\) by (3). All four
original edge blocks are positive there: these are the edges
of the positive unit-charge solution, including the two complete
outside incidences.

The [positive-edge Hessian theorem](research_positive_edge_global_monotonicity.md),
Theorem 1 and Theorem 3, proves
\(\Re(-\psi'')\succ0\) for each original positive edge on its
complete logarithmic branch. Restricting its outside coordinate
to zero keeps a strictly positive quadratic form in the inside
coordinate. Summing over the four edges in (8), every selected
coordinate is incident to an edge. The quadratic crossings have
purely imaginary constant Hessians. Therefore
\[
J:=-\mathcal H''(t_g,t_g,u_g),\qquad \Re J\succ0 .
                                                                    \tag{9}
\]
Here real part is both the entrywise real part and the Hermitian
part, since \(J\) is complex symmetric. This uses the actual
geometric angular Hessian, rather than nonsingularity of an
unrelated polynomial system.

Order the first two coordinates before \(u\), and write
\[
J=\begin{pmatrix}B&b\\ b^T&d\end{pmatrix}.
                                                                    \tag{10}
\]
The end block is diagonal, with entries
\(-\Phi_{0,tt}(t_g,u_g)\); it is invertible. Local elimination
of the two ends is exactly the selected branch in (7).
Consequently the reduced action is
\[
\Xi_0(u)=2S(-2,u)+iu^2/\pi-iu,\qquad
-\Xi_0''(u_g)=d-b^TB^{-1}b.
                                                                    \tag{11}
\]
To retain the sign of the Schur complement, let \(x=-B^{-1}b\).
Then
\[
d-b^TB^{-1}b
 =\begin{pmatrix}x\\1\end{pmatrix}^{\!*}
       J\begin{pmatrix}x\\1\end{pmatrix},
\qquad
\Re[-\Xi_0''(u_g)]>0 .
                                                                    \tag{12}
\]
The equality follows because the first block of
\(J(x,1)^T\) is zero. It is the exact positive-real-part
Schur argument of the same source, equation (36).
In particular the outer Hessian is nonzero, and an increasing
horizontal interval through \(u_g\) is a strict local Gaussian
contour. Equations (3),(7) also give \(\Xi_0'(u_g)=0\) with
the original unit charge.

## 3. Independent ordinary boundary deformation

For \(\mathbf w=(w_L,w_R)\) near \((-2,-2)\), put
\[
\Xi(u;\mathbf w)=S(w_L,u)+S(w_R,u)+iu^2/\pi-iu.
                                                                    \tag{13}
\]
The implicit function theorem and (12) give a unique
holomorphic critical point \(u_*(\mathbf w)\) near \(u_g\).
Shrink a fixed bidisk once so its image lies in a compact subset
of the interior of (5). It is the continuation of the original
point, and no new logarithmic root is chosen. Put
\[
\Theta(\mathbf w)=\Xi(u_*(\mathbf w);\mathbf w),\qquad
\mathcal B(\mathbf w)=i\sqrt{\frac2\pi}\,
\frac{\sin u_*(\mathbf w)\,
 A(w_L,u_*(\mathbf w))A(w_R,u_*(\mathbf w))}
 {\sqrt{-\Xi_{uu}(u_*(\mathbf w);\mathbf w)}} .
                                                                    \tag{14}
\]
The square root is the continuation of the horizontal Gaussian
root in (12), which has positive real part. All these functions
are holomorphic on a neighborhood of a smaller closed bidisk;
\(\mathcal B\) is nowhere zero there. In particular \(\sin u_g\ne0\)
by (4), and the other factors are already nonzero in (6),(12).

Choose a sufficiently small fixed \(\epsilon>0\) such that
\[
J_g=[u_g-\epsilon,u_g+\epsilon]
                                                                    \tag{15}
\]
and a neighborhood of it lie in the outgoing interior and the
strict local Hessian chart. This interval is fixed independently
of \(\mathbf w,N\). Define the literal local part of the outer
contour by
\[
\begin{split}
\mathcal L_N(\mathbf w)
 =-\frac{N^2C_{N,4}}{\pi i}
 \int_{J_g}&\sin u\,\mathscr Q_N(w_L,u)\mathscr Q_N(w_R,u)
          e^{iNu^2/\pi}W_N(u)\,du,\\
W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}.
\end{split}                                                       \tag{16}
\]
Both complete three-kernels and the entire sampling denominator
occur in this definition.

**Theorem.** There is a fixed ordinary bidisk about \((-2,-2)\)
on which, uniformly through both level parities,
\[
\boxed{\quad
\mathcal L_N(\mathbf w)
 =C_{N,4}C_{N,3}^{\,2}N^{-3/2}
     \mathcal B(\mathbf w)e^{N\Theta(\mathbf w)}
                         (1+O_{\rm hol}(N^{-1})).
\quad}                                                            \tag{17}
\]
Every fixed ordinary mixed derivative of its normalized relative
error is \(O(N^{-1})\) on smaller bidisks.

Indeed the exact normalized errors in (6) are holomorphic and
uniform on the neighborhood just chosen. Their product is retained
inside the integral. The common positive depth also gives
\[
W_N(u)=e^{-iNu}(1+O(e^{-cN})),\qquad c>0,
                                                                    \tag{18}
\]
on that neighborhood. This estimates the sum of all higher charges
there; it makes no assertion about charges on a remote contour.

At the complete colors, Taylor's theorem and (12), after shrinking
\(\epsilon\), give
\[
\Re\Xi_0(u_g+x)\le\Re\Xi_0(u_g)-c_0x^2
                       \quad(|x|\le\epsilon),\qquad c_0>0.
\]
For the smaller incoming bidisk, translate the middle part of
(15) horizontally through \(u_*(\mathbf w)\) and join it back to
the fixed endpoints. The finite integrand is holomorphic throughout
this local deformation, which remains strictly below all sampling
poles. Continuity preserves a fixed strict end loss on the short
joins and exterior parts, and preserves
\(\Re\Xi_{uu}<0\) on the central chart.
The local complex Gaussian calculation is therefore uniform.
Its exact powers and scalar are
\[
N^2\,N^{-3}\,N^{-1/2}=N^{-3/2},\qquad
-\frac1{\pi i}\sqrt{2\pi}=i\sqrt{2/\pi}.
                                                                    \tag{19}
\]
The remaining factors give exactly (14). This proves (17).
Since (16) has fixed endpoints and is holomorphic in both ordinary
colors, Cauchy's formula applied to the final normalized error
proves the derivative assertion. No derivatives of moving contour
endpoints are required.

The incoming action derivative from the inner theorem also gives
\[
\Theta_{w_L}(-2,-2)=\Theta_{w_R}(-2,-2)
                     =-\frac{\cos(t_g/2)}{4\pi}\ne0.
                                                                    \tag{20}
\]
The derivative of \(u_*(\mathbf w)\) contributes zero by stationarity.
For fixed integers \(j,k\ge0\), differentiating (17) consequently
gives at the complete colors
\[
\begin{split}
\partial_{w_L}^j\partial_{w_R}^k\mathcal L_N(-2,-2)
={}&C_{N,4}C_{N,3}^{\,2}N^{j+k-3/2}\mathcal B(-2,-2)\\
&\times\left\{-\frac{\cos(t_g/2)}{4\pi}\right\}^{j+k}
 e^{N\Xi_0(u_g)}(1+O(N^{-1})).
\end{split}                                                       \tag{21}
\]
These are derivatives of the specified local contribution.

## 4. Original action and an elementary rate floor

The [original action calibration](research_mixed_geometric_action_calibration.md),
equation (23), and
[geometric/source identification](research_mixed_geometric_source_identification.md)
give at the same actual point
\[
\mathcal F_{343}(z_{\rm geom})=\Xi_0(u_g)+2i\gamma,\qquad
2\pi\Re\Xi_0(u_g)=V_{\rm cells}.
                                                                    \tag{22}
\]
The real constant \(\gamma\) is exactly the original type-three
vertex constant; it has not been absorbed into a new primitive.
Thus one may rewrite (17) at completeness with exponent
\(\mathcal F_{343}\) only by retaining the additional unit scalar
\(e^{-2iN\gamma}\). Formula (17) uses the actual angular scalar
\(C_{N,4}C_{N,3}^2\) throughout. The marked volume interpretation
has precisely the scope of the original completion theorem.
No volume interpretation for arbitrary independent complex colors
is asserted by this local analytic deformation.

There is also a useful written lower bound. In the middle
identities of the height theorem, \(q_g=\Im\cos(t_g/2)>1/4\) implies,
with \(B=\cos\beta_g\) and \(L=\cosh K_g\),
\[
q_g=\sin\beta_g\{L-(L-B)^{-1}\}>1/4,\qquad
B<L-\frac1{L-1/4}.
\]
The bracket exceeds \(1/4\), since \(0<\sin\beta_g\le1\).
The height theorem proves \(L<157/125\), and the last expression
is increasing in \(L>1\). Consequently
\[
B<\frac{16471}{62875}<\frac3{10}
 <\cos(2\pi/5),\qquad \beta_g>2\pi/5 .
\]
The rational comparison is \(164710<188625\); the last strict
inequality uses \(\cos(2\pi/5)=(\sqrt5-1)/4\) and
\(\sqrt5>11/5\), whose square comparison is \(125>121\).
Using \(s_0(u_g)>321/200\) and \(K_g<7/10\) therefore gives
\[
\Re\Xi_0(u_g)
 =2s_0(u_g)+(2\beta_g/\pi-1)K_g
 >\frac{321}{100}-\frac7{50}=\frac{307}{100}.
                                                                    \tag{23}
\]
This is a lower bound on the original local action, not an estimate
of any outer remainder.

## 5. Exact remainder still required for closing

Take the height \(h=K_g\) in the
[complete Hermite contour identity](research_exact_complete_trace_contour.md).
For all boundary colors in the chosen bidisk set
\[
G_N(u;\mathbf w)=
\sin u\,\mathscr Q_N(w_L,u)\mathscr Q_N(w_R,u)e^{iNu^2/\pi}.
\]
The complete closing satisfies the exact identity
\[
Z_{343,N}(\mathbf w)=\mathcal L_N(\mathbf w)
                              +\mathcal R_N(\mathbf w),
                                                                    \tag{24}
\]
where, with both complementary horizontal pieces oriented rightward,
\[
\begin{split}
\mathcal R_N(\mathbf w)={}&
-\frac{N^2C_{N,4}}{\pi i}
\int_{[-\pi-iK_g,\,\pi-iK_g]\setminus J_g}
                       G_N(u;\mathbf w)W_N(u)\,du\\
&+\frac{\eta_NN^2C_{N,4}}{\pi}
\int_{-K_g}^{K_g}
       \frac{G_N(\pi+iv;\mathbf w)}{4\cosh^2(Nv/2)}\,dv .
\end{split}                                                       \tag{25}
\]
No far grid sample has been removed in (24)--(25). The original
odd central sample and all first normal data remain encoded in
this identity; the factor multiplying charge \(\ell\) in \(W_N\)
is still \(\ell\eta_N^{\ell-1}\).

A strict bound for the complete remainder (25), or a different
source-faithful non-cancellation argument, is still needed to
replace \(\mathcal L_N\) by \(Z_{343,N}\) in (17). The local
Gaussian does not give that bound. In particular (22) proves the
volume rate for this actual local term, not yet for the complete
ordinary closing. Uniform boundary control of that remainder
would be an additional requirement for a further composition
or short-partial-filling theorem.

## Frozen source bindings

- Exact symmetric contraction, unit charge and local scalar:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Full Hermite contour and all charge/endpoint factors:
  a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8.
- Positive geometric angular Hessian and Schur comparison:
  da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500.
- Actual positive unit solution:
  d3806cebb427d94b795e85c5c089592c4646b49ffc01238673f4f9d04f7f3bac.
- Original angle/root identification:
  0071c0fcb46fae09a0223f5c33542ff5424896a9c8eb3431dec9f378c4b3253f.
- Actual middle height below \(7/10\):
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
- Complete larger-rectangle inner packet:
  4e6d58951cff746a5daf6b3efcf3df917233e64d773d936a232dbc6bb870c96c.
- Ordinary incoming disk and normalized mixed derivatives:
  fedd23ea3d5d8aea8132af828f358bb0b0884e1e599a5dc31f457b33dd261aae.
- Original absolute action and marked volume calibration:
  7fd7032d085cb9055904673a7c3d9dd978a0fa19639670d5ece67ba8093e09d9.
- Original geometric/source identification:
  ac2b6c8993eeae51eb27a449a23f0524dc10a6f1e10b3b816446178754ea5f4b.
