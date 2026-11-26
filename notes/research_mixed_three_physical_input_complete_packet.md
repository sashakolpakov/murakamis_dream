# The complete twice-crossed packet at physical incoming rows

Research deduction, 7 November 2026. The initialized finite
reciprocal-factorial source has a nonzero complete asymptotic
on the actual real type-three incoming interval. Every original
summation row, both horizontal residue corrections, both entire
endpoint currents, and both joining segments are accounted for.
The retained second period is exponentially smaller, so the same
packet holds for the literal conditional polynomial and for the
whole Fourier boundary after two negative crossings.

The incoming arguments here are physical \(a=b/N\). The output
has a fixed complex neighborhood and uniform normalized
holomorphic derivatives. No fixed complex incoming neighborhood,
incoming derivatives, or arbitrary closing-functional estimate
is inferred. No numerical evaluation is used.

## 1. Statement with all source normalizations

Put
\[
 q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{(N-1)^2/2},\quad
 P_j=(r;r)_j,\quad p_j(U)=(rU;r)_j,
 \tag{1}
\]
and define the physical incoming set
\[
 \mathcal B_N=\left\{b\in\mathbb Z:0\le b<N,\
           \frac{267}{1000}\le\frac bN\le\frac{433}{1000}\right\}.
 \tag{2}
\]
The literal conditional polynomial is
\[
 C_{0,N}(X,W)=\sum_{j=0}^{N-1}
                      \frac{X^{-j}p_j(X)p_j(W)}{P_j^2}.
 \tag{3}
\]
Let \(J_N\) be the exact factorized representative of
[the initialized-source theorem](research_mixed_three_left_cycle_initialized_source.md),
and let \(\Phi_1(a,y)\) be the original left conditional critical
action, with the absolute constant fixed in
[the calibrated observation](research_mixed_three_fourier_calibrated_homogeneous_observation.md).
Write \(t_*=-z_2\), where \(z_2\) is the complete second-period
critical index. Set
\[
 \mathcal F(t;a,y)
   =-g(a-t)-2g(t)-g(y-t)
                     +\pi i\{a-(a-t)^2-t^2\},
 \tag{4}
\]
on its original regular critical chart, and
\[
 \mathcal C_J(a,y)=
  \frac{\sqrt{2\pi}\,e^{-\pi ia}}
  {\mathfrak a(a-t_*)\mathfrak a(t_*)^2
   \mathfrak a(y-t_*)\sqrt{-\mathcal F_{tt}(t_*;a,y)}} .
 \tag{5}
\]
All three factorial arguments in (5) have real part in \((0,1)\).
The square root has positive real part, and
\(\mathcal C_J\ne0\).

**Theorem 1.** There is a fixed complex neighborhood \(U\) of
\(y=x_0\) such that, uniformly for \(b\in\mathcal B_N\), both
level parities, and \(y\) in smaller fixed neighborhoods,
\[
\boxed{\begin{split}
 J_N(b/N,y)
   &=N^{-1/2}\mathcal C_J(b/N,y)e^{N\Phi_1(b/N,y)}
                                  (1+O(N^{-1})),\\
 C_{0,N}(r^b,e^{-2\pi iy})
   &=N^{-1/2}\mathcal C_J(b/N,y)e^{N\Phi_1(b/N,y)}
                                  (1+O(N^{-1})).
\end{split}}
 \tag{6}
\]
The normalized errors are holomorphic in \(y\); every fixed
outgoing derivative of them is \(O(N^{-1})\), uniformly in \(b\).
In particular the literal \(C_0\) source is nonzero there for all
sufficiently large levels, and there are constants \(c,C>0\) with
\[
 cN^{-1/2}e^{N\Re\Phi_1(b/N,y)}
 \le |C_{0,N}(r^b,e^{-2\pi iy})|
 \le CN^{-1/2}e^{N\Re\Phi_1(b/N,y)} .
 \tag{7}
\]

Use \(Z_N^{\rm cap}\) for the original full Fourier cap, to
distinguish it from the second period. Its exact conventions are
\[
\begin{split}
 Y&=e^{2\pi iy},\\
 f_l(y)&=\frac{e^{-\pi i(N-1)y}}N\,
                 Y^l\prod_{h=l+1}^{N-1}(1-Yr^h),\\
 Z_N^{\rm cap}(a,y)&=
       \sum_{l=0}^{N-1}C_{1,N}(e^{-2\pi ia},r^l)f_l(y).
\end{split}
 \tag{8}
\]
Here \(C_{1,N}\) is the same literal sum as (3), with \(P_j^3\)
in place of \(P_j^2\) in the denominator.
There is no additional crossing scalar in (8).
For the original signed output-crossing operator \(\mathcal M_{-2}\),
the full crossed boundary consequently satisfies
\[
 \boxed{\quad
 \mathcal M_{-2}Z_N^{\rm cap}(b/N,y)
   =\kappa^{-2}N^{-3/2}e^{-\pi iy}
       \mathcal C_J(b/N,y)
       e^{N\{\Phi_1(b/N,y)+\pi iy\}}(1+O(N^{-1})).
 \quad}
 \tag{9}
\]
The outgoing normalized derivatives and two-sided bounds hold
with the corresponding phase and powers in (9).

## 2. Every original finite contour contribution

At each physical \(a=b/N\), the initialized-source theorem gives
the exact complete sum
\[
 J_N(b/N,y)=\sum_{k=0}^{b}\mathscr T_{N,b}(k/N;y),
 \tag{10}
\]
where
\[
 \mathscr T_{N,b}(t;y)
  =N e^{\pi iNa-\pi iN[(a-t)^2+t^2]-\pi ia}
                     E_N(a-t)E_N(t)^2E_N(y-t).
 \tag{11}
\]
This identity retains the true finite interval, including both
endpoint rows. The reciprocal zeros of \(E_N(y-t)\) are not
removed when its real argument becomes negative.

The exact residue formula in
[the left-contour theorem](research_mixed_three_left_cycle_left_contour.md),
equations (12)--(13), gives
\[
\begin{split}
 J_N={}&
 N\int_{\alpha_N+ih_*}^{\beta_{N,b}+ih_*}
                                      \mathscr T_{N,b}(t;y)\,dt\\
 &+iN\int_{\mathbb R}w_{N,0}(v)
       \{\mathscr T_{N,b}(\beta_{N,b}+iv;y)
                    -\mathscr T_{N,b}(\alpha_N+iv;y)\}\,dv\\
 &+iN\int_0^{h_*}
       \{\mathscr T_{N,b}(\alpha_N+iv;y)
                    -\mathscr T_{N,b}(\beta_{N,b}+iv;y)\}\,dv ,
\end{split}
 \tag{12}
\]
with
\[
 \alpha_N=-1/(2N),\quad \beta_{N,b}=a+1/(2N),\quad
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}-\mathbf1_{\{v<0\}} .
 \]
Both original horizontal residue corrections have already been
sent to infinity with their exact fixed-level decay rates
\(2\pi(b+1)\) and \(2\pi(N\Re y+1)\).
No large-level bound was substituted for that exact limiting
identity.

The entire left weighted current in (12) has the uniform bound
\[
 N\int_{\mathbb R}|w_{N,0}(v)\mathscr T_{N,b}(\alpha_N+iv;y)|\,dv
                            \le CN^{-1}e^{N\Re\Omega(a,y)} .
 \tag{13}
\]
Since \(\Phi_1+\Psi_2=\Omega\) absolutely and the complete second
period has \(\Re\Psi_2\le-\gamma<0\) on the compact family,
(13) is exponentially below \(e^{N\Re\Phi_1}\).
The same theorem pays the unweighted left join by its strict
critical-height endpoint gap.

The full right-contour theorem
[including both infinite tails](research_mixed_three_left_cycle_right_contour.md),
equation (35), gives
\[
\begin{split}
 &N\int_{\mathbb R}
 |w_{N,0}(v)\mathscr T_{N,b}(\beta_{N,b}+iv;y)|\,dv\\
 &\qquad+N\int_0^{h_*}|\mathscr T_{N,b}(\beta_{N,b}+iv;y)|\,dv
                         \le CN^{-1}e^{N E_R(a,y)} .
\end{split}
 \tag{14}
\]
The original upper-branch endpoint rate satisfies
\[
                         E_R<\Re\Phi_1-1/20
 \tag{15}
\]
by [the endpoint-value theorem](research_mixed_three_left_cycle_right_endpoint_gap.md).
These are bounds on the complete currents, not just on bounded
vertical segments or on the last physical row.

Finally, the raised main segment has exactly one maximum,
at \(t_*\). On \(0<\Re t<\xi\), its original real phase is
strictly concave. On \(\xi\le\Re t\le a\), the exact distance
inequality of the right-contour theorem makes it strictly
decreasing. The inequalities \(0<h_*<\Im y\) keep each factorial
argument away from the real axis on this whole raised segment.
Thus the global upper/lower factorial expansions apply across
the shifted real walls, including the \(O(N^{-1})\) half-grid
extensions at either end. They preserve the strict endpoint gaps.

The local row has power \(N^{-1}\), coefficient
\[
       \frac{e^{-\pi ia}}
       {\mathfrak a(a-t)\mathfrak a(t)^2\mathfrak a(y-t)},
 \]
and critical action \(\mathcal F(t_*)=\Phi_1\).
Multiplication by the exact lattice density \(N\) and the
one-dimensional Gaussian gives (5) and the first line of (6).
The contour is oriented from left to right.
The odd \(N^{-1/2}\) terms after local rescaling cancel on a
symmetric neighborhood; the remaining symbol and Gaussian
expansion has relative error \(O(N^{-1})\).
Every complementary part of (12) has a strict exponential gap.

## 3. The retained period and the whole original crossed source

The initialized-source theorem is an exact identity for every
physical incoming row:
\[
 C_{0,N}(r^b,W)
       =J_N(b/N,y)-N(W^N-1)\mathcal I_{2,N}(b/N,y),
             \qquad W=e^{-2\pi iy}.
 \tag{16}
\]
The [real-input action-gap theorem](research_mixed_three_real_input_action_gap.md)
proves, on a fixed neighborhood of the real incoming family,
\[
 |N(W^N-1)\mathcal I_{2,N}(a,y)|
           \le CN^{-1/2}e^{N(\Re\Phi_1(a,y)-1/25)} .
 \tag{17}
\]
It retains the entire multiplier
\(W^N-1=e^{-2\pi iNy}(1-e^{2\pi iNy})\);
no division by a periodic zero is used.
Combining (16)--(17) with the first packet proves the second
line of (6).
At these physical incoming values the original particular forcing
vanishes identically in the free output. Hence
\(H_N(b/N,y)=C_{0,N}(r^b,W)\), and the same packet holds for
the actual homogeneous remainder at these physical rows.

The exact full-source identity from
[two negative crossings](research_mixed_fourier_negative_crossing_full_sources.md),
equation (14), is
\[
 \mathcal M_{-2}Z_N^{\rm cap}(a,y)
    =\frac{\kappa^{-2}e^{\pi i(N-1)y}}N
                         C_{0,N}(e^{-2\pi ia},e^{-2\pi iy}).
 \tag{18}
\]
It acts on the whole Fourier function, with all channels retained.
Substitution of (6) gives exactly (9). In particular the action
acquires \(+\pi iy\), the leading coefficient acquires
\(e^{-\pi iy}\), and the power becomes \(N^{-3/2}\).
All original \(\kappa\), cardinal, and chirp factors remain.

## 4. Holomorphic output errors and scope

All strict compact gaps used above persist on one sufficiently
small complex output neighborhood. The same exact charts retain
the moving reciprocal zeros. The critical branches and
coefficient (5) are holomorphic and nonzero there.
The finite raised segment can be moved through the perturbed
critical point; both joining segments in (12) remain present
and keep their gaps. The fixed-height tail cutoffs can be chosen
uniformly before varying \(N\).

These arguments give the estimates on a slightly larger output
neighborhood than the one used in (6). The normalized errors are
holomorphic functions of \(y\), so Cauchy's inequalities give all
fixed outgoing derivatives with the same \(O(N^{-1})\) order.
Uniform lower bounds for \(|\mathcal C_J|\), followed by increasing
\(N_0\), prove (7) and the corresponding bounds for (9).

The physical index \(b\) and its summation endpoint have not been
continued as a complex variable. In particular, these outgoing
jets are not incoming derivatives or arbitrary ordinary boundary
normals. The full physical node matrix still uses the original
linear node/Hermite adapters. A subsequent signed attachment,
incoming contour deformation, or prescribed knot closing sum
requires its own complete-source estimate; it cannot be justified
by multiplying these pointwise physical-row asymptotics through
a potentially cancelling observation.
