# A uniform combined-action bound from the positive transition weights

Private written source/rate deduction, 9 November 2026. The exact
positive Newton-to-Chebyshev transition gives an explicit outgoing
coefficient saving at every frequency. Combined with the selected
charged-action loss, it gives the same fixed saving \(5\pi/226\)
throughout the whole frequency interval. No coefficient phase or
positivity of an outgoing coefficient is asserted.

The remaining sufficient comparison is the correlated inequality
\(M_3+\mathcal E(1/2,Z_*)-\Lambda<5\pi/226\). It is not proved
here. The action comparison below is independent of any extension
of the finite outer-mode theorem. No mathematical numerical
evaluation, saved-value arithmetic, or frozen-source edit is used.

## 1. Exact source, original actions, and statement

Use the full source and both-parity coefficient normalization of
[the positive transition theorem, (1), (14), and (25)--(29)](research_mixed_next_outgoing_positive_chebyshev_transition.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
q=e^{i\pi/N},\quad r=q^{-2},\quad \kappa_N=q^{D^2/2},\\
C_{b,N}(Z)=\sum_{\ell=0}^{D-b}
 \frac{r^{-b\ell}(r^{b+1};r)_\ell(rZ;r)_\ell}{(r;r)_\ell^2},
\qquad C_{D,N}=1,\\
P_b^{\rm rad}(X)=e_b(X)/e_M(X),\qquad
F_N^+(X,Z)=\sum_{b=M}^{D}(-q)^bC_{b,N}(Z)P_b^{\rm rad}(X)
         =\sum_{k=0}^{U}f_{k,N}(Z)T_k(-X/2),\\
f_{k,N}(Z)=(-1)^{M+k}
       \sum_{d=k}^{U}q^{M+d}\beta_{d,k,N}C_{M+d,N}(Z),
\qquad \beta_{d,k,N}>0.
\end{gathered}                                                     \tag{1}
\]
The conditional sum is complete, including its literal stopping
factors. The radical quotient is an ordinary polynomial. All
conditional phases in the last line remain present.

Let \(Z_*=e^{-2\pi iz_*}\) be the outgoing value of an actual
complete word in powers three and four beginning \(343\), of
length at least five. Keep the original outgoing action
\[
E_0(Z_*)=\mathcal E(1/2,Z_*),\qquad
\mathcal E(a,Z_*)=-\int_a^1\log|\mathcal L(v,Z_*)|\,dv,
\quad 1/2\le a\le1.                                             \tag{2}
\]
Here \(\mathcal L\) is the selected finite-ratio limit and the
terminal normalization is \(\mathcal E(1,Z_*)=0\). The
[sharper-tail theorem, (16)](research_mixed_next_outgoing_sharper_tail_and_ellipse.md)
proves
\[
\mathcal E(1/2+x,Z_*)\le E_0(Z_*)-c_*x,\qquad
c_*=\frac{205}{1134},\qquad 0\le x\le1/2.                        \tag{3}
\]
This is an integrated chord estimate; no constant pointwise
upper bound for \(\partial_a\mathcal E\) is substituted for it.

Set
\[
\begin{split}
J(v)&=\int_0^v\log(2\sin\pi s)\,ds,\qquad J(0)=J(1/2)=J(1)=0,\\
\mathcal H(x,t)&=J(2x)-J(x-t)-J(x+t)-2J(1/2+x),\\
\mathcal D(t,Z_*)&=\max_{t\le x\le1/2}
 \{\mathcal E(1/2+x,Z_*)+\mathcal H(x,t)\},
\qquad 0\le t\le1/2.
\end{split}                                                       \tag{4}
\]
The finite transition theorem proves, uniformly at both parities
and every \(0\le k\le U\),
\[
|f_{k,N}(Z_*)|\le CN^A e^{N\mathcal D(k/N,Z_*)}.                  \tag{5}
\]
Its endpoint-uniform sine-product proof already includes all
half-index shifts, \(k=0\), \(k=U\), and \(b=D\).

Use the original selected charged action
\[
\Gamma(\delta)=\Re\!\left\{
S(u_\delta)+\frac{3iu_\delta^2}{4\pi}-i\delta u_\delta\right\},
\qquad M_3=\Re S(0),\qquad 0\le\delta\le1/2.                    \tag{6}
\]
The [charged quadratic-loss theorem](research_mixed_next_selected_charged_quadratic_loss.md)
gives
\[
\Gamma(\delta)\le M_3-b_*\delta^2,\qquad
b_*=\frac{10\pi}{113},                                         \tag{7}
\]
with strict inequality for \(\delta>0\).

**Theorem.** On the complete interval \(0\le t\le1/2\),
\[
\boxed{\quad
\mathcal D(t,Z_*)\le E_0(Z_*)-b_*t(1-t).
\quad}                                                         \tag{8}
\]
Consequently
\[
\boxed{\quad
\sup_{0\le t\le1/2}
 \{\mathcal D(t,Z_*)+\Gamma(1/2-t)\}
\le E_0(Z_*)+M_3-\frac{5\pi}{226}.
\quad}                                                         \tag{9}
\]
In particular the actual finite outgoing coefficients obey
\[
|f_{k,N}(Z_*)|
 \le CN^A\exp\!\left\{N\left[
 E_0(Z_*)-\frac{10\pi}{113}\frac{k}{N}
                         \left(1-\frac{k}{N}\right)\right]\right\}.
                                                                  \tag{10}
\]
This is a bound on the original signed coefficient in (1),
obtained by an eligible absolute upper bound on that finite sum.

## 2. Curvature of the exact transition rate

For \(0\le t<x<1/2\), direct differentiation in (4) gives
\[
\partial_t\mathcal H(x,t)
 =\log\frac{\sin\pi(x-t)}{\sin\pi(x+t)},\qquad
\partial_t^2\mathcal H(x,t)
 =-\frac{2\pi\cot(\pi x)}
       {1-\sin^2(\pi t)/\sin^2(\pi x)}.                          \tag{11}
\]
The first derivative at \(t=0\) is zero, and the exact transition
identity gives \(\mathcal H(x,0)=0\). The denominator in (11)
belongs to \((0,1]\). Integrating the resulting second-derivative
inequality twice therefore yields
\[
                 -\mathcal H(x,t)\ge\pi t^2\cot(\pi x).
                                                                  \tag{12}
\]
Continuity of \(J\) extends this bound to \(t=x<1/2\) and to
\(x=1/2\), where \(\mathcal H(1/2,t)=0\). The remaining point
\((x,t)=(0,0)\) is handled by its exact zero value. Thus no
derivative of \(J\) at a singular endpoint is required.

Two elementary lower bounds for the cotangent will be useful:
\[
\cot(\pi x)\ge\frac{1-2x}{\pi x},\qquad
\cot(\pi x)\ge\pi(1/2-x),\qquad 0<x\le1/2.                     \tag{13}
\]
For the first, concavity gives \(\cos\pi x\ge1-2x\), while
\(\sin\pi x\le\pi x\). The second is
\(\tan(\pi(1/2-x))\ge\pi(1/2-x)\).

## 3. A uniform transition-plus-chord cost

We claim that
\[
c_*x-\mathcal H(x,t)\ge b_*t(1-t),
\qquad 0\le t\le x\le1/2.                                     \tag{14}
\]
The comparisons of constants used below are written explicitly:
\[
c_*>\frac4{25},\qquad
c_*=\frac9{50}+\frac{11}{14175}>\frac9{50},\qquad
c_*<\frac15,\qquad
b_*<\frac{220}{791}<\frac3{10}.                               \tag{15}
\]
The first and third follow from \(5125>4536\) and
\(1025<1134\). The last uses \(\pi<22/7\) and \(2200<2373\).

First suppose \(0<t\le1/4\). From (12) and the first bound
in (13),
\[
\begin{split}
c_*x-\mathcal H(x,t)
&\ge c_*x+\frac{t^2}{x}-2t^2\\
&\ge2\sqrt{c_*}\,t-2t^2
 >\frac45t-2t^2
 \ge\frac3{10}t
 >b_*t(1-t).
\end{split}                                                     \tag{16}
\]
The second line is the arithmetic-geometric mean inequality;
its strict comparison uses \(c_*>4/25\).

Now suppose \(1/4\le t\le x\le1/2\). The second bound in (13)
gives
\[
\begin{split}
c_*x-\mathcal H(x,t)
&\ge c_*x+\pi^2t^2(1/2-x)\\
&\ge c_*x+c_*(1/2-x)=c_*/2\\
&>\frac9{100}>\frac3{40}>b_*/4\ge b_*t(1-t).
\end{split}                                                     \tag{17}
\]
Here \(\pi^2t^2\ge9/16>1/5>c_*\), using \(\pi>3\).
The comparison \(9/100>3/40\) is \(360>300\).
For \(t=0\), (14) is simply \(c_*x\ge0\), since
\(\mathcal H(x,0)=0\). This proves (14), including every boundary.

Combining (3) and (14), then maximizing over \(x\), proves
(8). The stronger estimates (16) and (17) are available
separately; in particular the transition cost does not disappear
at the high-frequency endpoint.

## 4. Combination and the exact remaining comparison

By (7) and (8),
\[
\begin{split}
\mathcal D(t,Z_*)+\Gamma(1/2-t)
&\le E_0(Z_*)+M_3
       -b_*\{t(1-t)+(1/2-t)^2\}\\
&=E_0(Z_*)+M_3-b_*/4.
\end{split}                                                     \tag{18}
\]
The identity inside braces is exactly \(1/4\), proving (9).
All rates are the original normalized actions.

Define the actual correlated excess
\[
\mathfrak E_*=M_3+E_0(Z_*)-\Lambda.                              \tag{19}
\]
An actual bound
\[
                     \mathfrak E_*<5\pi/226                    \tag{20}
\]
with a fixed margin would therefore pay the entire combined
envelope, and hence also the remaining interval
\(0\le t\le15/32\). The already-paid terminal finite block is
unchanged. No new estimate for that block is needed.

The zero-frequency endpoint gives a separate necessary condition
for the requested envelope comparison:
\[
\begin{split}
\mathcal D(0,Z_*)+\Gamma(1/2)<\Lambda
&\quad\Longleftrightarrow\quad
\mathfrak E_*<M_3-\Gamma(1/2),
\end{split}                                                     \tag{21}
\]
because \(\mathcal D(0,Z_*)=E_0(Z_*)\). This is a condition
on the upper envelope, not a lower bound for the actual signed
constant coefficient or for the attached observation. Nor does
(9) assert that the maximum of the exact combined envelope
occurs at \(t=0\).

The [harmonic-disk theorem](research_mixed_next_attachment_excess_harmonic_disks.md)
identifies (19), at every actual reference, with
\[
\mathfrak E(b)=M_3+\Re\{\mathcal S_{\rm h}(z(b))-\Pi(b)\}.
                                                                  \tag{22}
\]
It proves that the maximum on each of the two original complete
parameter disks occurs on its boundary circle. Thus a uniform
upper bound \(5\pi/226\) on those two correlated circles would
suffice for (20). That circle bound is not inferred here.

For comparison, the
[half-input source ceiling](research_mixed_next_actual_half_input_outgoing_ceiling.md)
and complete outgoing anchor imply
\[
E_0(Z_*)\le\Lambda-\frac{17}{10}.                               \tag{23}
\]
Indeed, at the original last double node \(c_U\), every reversed
Newton amplitude term of positive degree vanishes, so the
full version \(H_N^{\rm all}(c_U,Z_*)\) is exactly \(C_{M,N}(Z_*)\).
The finite ceiling and absolute anchor, followed by
\(M/N\to1/2\), give (23). This step uses the full conditional
source and does not infer a lower bound from a contour majorant.
Together with the original complete-action bound \(M_3<121/63\),
it yields only
\[
                     \mathfrak E_*<\frac{139}{630}.             \tag{24}
\]
This does not imply (20):
\(139/630>1/5>3/40>5\pi/226\), with the last comparison already
contained in (15). The deficiency is in this certified upper
comparison; no lower bound on the actual excess is asserted.

The exact final source remains
\[
\frac1{\kappa_N^2N}\mathcal L_N(F_N^+),\qquad
\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F].                 \tag{25}
\]
Its full Hermite source, first normals, odd simple node, both
parities, and every outgoing row in (1) remain present. Applying
(9) to it requires the independently proved finite outer-mode
upper bound at \(\Gamma(1/2-k/N)\), with the original sampling
currents and scalar. Equation (9) alone is an action-envelope
theorem, while (10) is already an unconditional finite outgoing
coefficient theorem. Neither proves the remaining reference
estimate or stability under arbitrary fixed short fillings.

## Frozen source bindings

- Exact positive transition and full coefficient normalization:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Complete outgoing chord and terminal action:
  fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3.
- Original selected charged quadratic loss:
  f8a3e8729e2325e151fc4b05d33d917e739b82c5157aff3cd9b8ee0f85f8b0f5.
- Actual half-input source ceiling:
  ecf0b292a5fcc7ecf962ac74f77a0a6293cf49008035c7f3672da7182999134a.
- Complete outgoing absolute anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Correlated harmonic reduction:
  623ebfda0574d46a7e10e851d27a9fd48a8910543691a58a8d819a882878be47.
- Original complete-action upper bound:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Terminal mode payment and unchanged full observation:
  7a0a060b8313d250d7b0e49d181f5242f4a47b0a3d56d19d542f60497f323587.
