# Exact scalar optimization of the original horizontal real cuts

Research reduction, 5 November 2026. For either original real cut,
the allocated rate minus the original outer supporting plane separates
into two strictly concave scalar functions. Each maximum is attained
at an explicitly clipped endpoint or at one admissible root of a
quadratic or sextic equation. This is an exact reduction of the missing
cut estimate, not a newly certified uniform cut gap or a complete
horizontal finite-source theorem.

## 1. The original allocation and its scalar factors

Use the original primitive
\(g'(z)=\operatorname{Log}(1-e^{-2\pi iz})\), with the same
regular-strip branch and absolute constant as in the
[fixed zero-mode lemma](research_mixed_horizontal_zero_mode_support.md).
Fix an actual original conditional reference
\((s_0,a_0,b_0)\), and write
\[
 \begin{split}
 a_0=x_0+ih_a,\qquad b_0=y_0+ih_b,\qquad
 I=[11/50,9/20],\qquad |h_a|,|h_b|\le3/25,\\
 F(s,a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
       -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi ias,\\
 M=\Re F(s_0,a_0,b_0),\qquad
 p_a=\Re F_a(s_0,a_0,b_0),\qquad
 p_b=\Re F_b(s_0,a_0,b_0).
 \end{split}
 \tag{1}
\]
Here \(\eta,\epsilon\in\{0,1\}\), and the reference real
coordinates belong to \(I\). The original index equation is
\(F_s(s_0,a_0,b_0)=0\), so these are the original allocated
critical-phase marginals, not marginals at the cut.

For a real \(s\in[3/20,49/100]\), define
\[
 f_{s,h,\lambda,d}(x)
 =\Re\{g(s+x+ih)-\lambda g(x+ih)+2\pi ids(x+ih)\},
 \quad \lambda\in\{1,3/2\},\quad d\in\{0,1\}.
 \tag{2}
\]
The last term equals \(-2\pi dsh\), independent of \(x\).
For the first factor use \((h,\lambda,d)=(h_a,1+\eta/2,1)\);
for the second use \((h_b,1+\epsilon/2,0)\). Denote these
functions by \(f_a,f_b\). Thus the two-variable cut rate is
exactly their sum plus the constant
\(-(2+\epsilon)\Re g(s)\). All argument real parts and all
shifted real parts lie strictly between zero and one; no logarithmic
wall or change of the original lift occurs on this domain.

## 2. Strict concavity on the full real plateau

Put \(u=\cot\pi s>0\) and
\(p+i\beta=\cot\pi(x+ih)\). The elementary bounds in the
fixed zero-mode lemma give
\[
 0<u<2,\qquad 9/70<p<3/2,\qquad |\beta|<4/5.
 \tag{3}
\]
For \(C=\Re\cot\pi(s+x+ih)\), the cotangent addition
identity gives the exact positive numerator
\[
 p-C=
 \frac{(u+p)(p^2+1-\beta^2)+2p\beta^2}
      {(u+p)^2+\beta^2}.
 \tag{4}
\]
Its denominator is less than \(13\). Its numerator is greater
than \((9/70)(9/25)\). Since
\(g''(z)=\pi\cot\pi z-\pi i\),
\[
 -f''(x)=\pi(\lambda p-C)
 >\frac{81\pi}{22750}
 >\frac{243}{22750}>\kappa,\qquad \kappa=1/100.
 \tag{5}
\]
This holds for every \(x\in I\), both signs of the fixed
height, both allocations, and every real \(s\) in the stated
interval. In particular it covers both actual cuts
\(s_-=3/20\) and \(s_+=49/100\). It does not assert
horizontal concavity of arbitrary right-tail rows: their shifted
argument may cross a numerator wall, outside this regular strip.

## 3. Clipped maximizers and algebraic stationarity

For either factor, let \(x_0\) be its reference real coordinate
and \(p_0\) its original real marginal. Define
\[
 \begin{split}
 B(x)&=f(x)-f(x_0)-p_0(x-x_0),\\
 G&=\max_{x\in I}B(x)\ge0.
 \end{split}
 \tag{6}
\]
Strict concavity implies that the unique maximizer \(x_*\) is:

* the left endpoint if \(f'(11/50)\le p_0\);
* the right endpoint if \(f'(9/20)\ge p_0\);
* otherwise the unique interior solution of \(f'(x_*)=p_0\).

These cases include equality at an endpoint. There is no need to
choose among multiple admissible stationary branches.

The interior equation is algebraic in \(v=\tan\pi x>0\).
Set \(r=e^{2\pi h}>0\), \(c_s=\cos2\pi s\),
\(t_s=\sin2\pi s\), and
\[
 \begin{split}
 D(v)&=(1-r)^2+(1+r)^2v^2,\\
 N_s(v)&=1+r^2-2rc_s+4rt_sv+(1+r^2+2rc_s)v^2.
 \end{split}
 \tag{7}
\]
Then
\[
 |1-e^{-2\pi i(x+ih)}|^2=\frac{D(v)}{1+v^2},\qquad
 |1-e^{-2\pi i(s+x+ih)}|^2=\frac{N_s(v)}{1+v^2}.
 \tag{8}
\]
Both numerators are strictly positive on
\(v\in[\tan(11\pi/50),\tan(9\pi/20)]\), including
\(h=0\). Taking real parts of the original logarithms shows
that \(f'(x)=p_0\) is equivalent to
\[
 \begin{cases}
 N_s(v)-e^{2p_0}D(v)=0,&\lambda=1,\\
 N_s(v)^2(1+v^2)-e^{4p_0}D(v)^3=0,&\lambda=3/2.
 \end{cases}
 \tag{9}
\]
These have degree at most two and six, respectively. The squaring
in the second equation is reversible because both sides before
squaring are positive. Roots outside the displayed interval have
no role. Within it there is at most one root, by (5). The word
"algebraic" here refers to the polynomial in \(v\); its
coefficients still contain the actual height and original marginal.
No algebraicity or independently released bound for those reference
data is assumed.

## 4. Exact cut deficits and a direct upper bound

At either cut define its actual reference gap and the two scalar
gains from (6):
\[
 \delta_s=M-\Re F(s,a_0,b_0),\qquad G_a(s),\quad G_b(s).
 \tag{10}
\]
Separation gives the exact identity
\[
 \max_{x,y\in I}
 \{\Re F(s,x+ih_a,y+ih_b)-M
      -p_a(x-x_0)-p_b(y-y_0)\}
 =-\delta_s+G_a(s)+G_b(s).
 \tag{11}
\]
Thus the whole cut is below the original affine plane with reserve
\(\gamma\) precisely when
\(G_a(s)+G_b(s)\le\delta_s-\gamma\). This condition
uses the same actual coupled reference in all three terms. In
particular the already proved positive reference cut gap does not,
by itself, pay the nonnegative gains in (11).

There is also a bound requiring no stationary equation. Write
\(b=f'(x_0)-p_0\) and
\(\widehat d=\operatorname{proj}_{[11/50-x_0,\,9/20-x_0]}(b/\kappa)\).
Integrating (5) gives
\[
 G\le b\widehat d-\frac\kappa2\widehat d^2
 \le\frac{b^2}{2\kappa}.
 \tag{12}
\]
The exact slopes against the original conditional reference are
\[
 \begin{split}
 b_a&=\Re\{g'(s+a_0)-g'(s_0+a_0)\}+2\pi\Im s_0,\\
 b_b&=\Re\{g'(s+b_0)-g'(s_0+b_0)\}.
 \end{split}
 \tag{13}
\]
The asymmetric extra term is the original first-argument chirp;
dropping it would change the supporting-plane problem.

For a bound with a quadratic outer loss \(\zeta>0\), replace
\(B(x)\) by \(B(x)+\zeta(x-x_0)^2/2\). If
\(0<\zeta<\kappa\), it remains strictly concave. Equation (11)
holds with these modified gains when its maximand also includes
\(\zeta\{(x-x_0)^2+(y-y_0)^2\}/2\). Bound (12) then uses
\(\kappa-\zeta\). The modified stationary equation includes
the linear displacement term and is not asserted to remain the
polynomial (9).

## 5. Source scope

At the real cuts the original regular-strip finite-source rate is
exactly the allocation (1), with its original first chirp and both
outer Fourier halfweights. For unselected type-four outer arguments,
keep their actual negative reference heights, as in the fixed
zero-mode lemma, so the factorial branch is the relevant Fourier
upper rate. The present optimization preserves that allocation and
the complete original reference constant. Linear Fourier corrections
at a fixed height are constant in the real coordinate, so the same
scalar maximizer rule also applies to each separately specified
branch; branch constants must still be retained before taking their
maximum.

No new bound on (11) over all actual references is claimed. Even
after such a bound, real tails, vertical joins and both aliases need
their respective source estimates. Equations (6)--(13) reduce one
specific missing comparison without substituting a moving root or
turning a central zero-mode estimate into a complete kernel theorem.
