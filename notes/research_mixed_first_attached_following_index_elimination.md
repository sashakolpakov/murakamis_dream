# Exact following-index elimination and a limit of the affine credit

Research deduction, 7 November 2026. The entire following regular
index rectangle reduces to two prescribed real endpoints and their
specified height endpoints. This is valid both at the actual
neighbor height and in the conservative zero-height comparison.
Neither following branch is discarded.

The resulting affine-credit test is not positive on its full
containing coefficient rectangle. Section 3 proves this with an
exact analytic witness. That witness concerns a conservative lower
expression; it is neither an actual-source counterexample nor an
assertion that its separately bounded reference coefficients occur
simultaneously in the coupled canonical family.

## 1. The entire following rectangle

Use the original derivative, allocations and source restrictions of
[the neighbor-height theorem](research_mixed_first_attached_neighbor_height_credit.md).
Fix the actual neighbor \(b=z+ih\), with
\[
 .1\le z\le.5,\qquad -.108\le h\le0,
 \qquad t=w+i\zeta,\quad
 .22\le w\le.49,\quad -.108\le\zeta\le.068 .
 \tag{1}
\]
Write \(A(y,R)=\arg(1-Re^{-2\pi iy})\) on the original
logarithmic lift. All shifted real arguments below belong
to \([.32,.99]\), so none is an integer or a logarithmic
zero. Put
\[
 \zeta_-(z)=
 \begin{cases}
 -.108,&z<.28,\\
 .068,&z>.28,
 \end{cases}
 \qquad
 \begin{split}
 G_-(z,h)&=.44\pi+
      A(.22+z,e^{2\pi(h+\zeta_-(z))}),\\
 G_+(z,h)&=.98\pi+
      A(.49+z,e^{2\pi(h+.068)}).
 \end{split}
 \tag{2}
\]
At \(z=.28\), either value of \(\zeta_-\) gives the
same result \(G_-=.44\pi\).

**Lemma 1.** Exactly,
\[
 \min_{\substack{.22\le w\le.49\\-.108\le\zeta\le.068}}
 \Im\{g'(t+b)+2\pi it\}
                         =\min\{G_-(z,h),G_+(z,h)\}.
 \tag{3}
\]

*Proof.* At fixed \(\zeta\), set
\(R=e^{2\pi(h+\zeta)}>0\), \(\theta=2\pi(w+z)\).
The expression being minimized is
\[
                         2\pi w+A(w+z,R).
 \tag{4}
\]
Its derivative in \(w\) is
\[
              \frac{2\pi(1-R\cos\theta)}
                         {1+R^2-2R\cos\theta}.
 \tag{5}
\]
If \(R\le1\), (5) is positive on the present regular
interval. If \(R>1\), a zero requires
\(\cos\theta=1/R>0\).
Here \(.64\pi\le\theta\le1.98\pi\); every such zero
is therefore in \((3\pi/2,2\pi)\).
The derivative of \(1-R\cos\theta\) in \(\theta\) is
\(R\sin\theta<0\) there. Every zero in (5) is a
downward crossing and hence a strict local maximum of (4).
Its minimum in \(w\) is consequently at \(.22\) or \(.49\).

At either real endpoint, differentiation in \(\zeta\) gives
\[
 \partial_\zeta A(w+z,e^{2\pi(h+\zeta)})
   =\pi\Re\cot\pi(w+z+i(h+\zeta)).
 \tag{6}
\]
Its sign is the sign of \(\sin2\pi(w+z)\), independently
of height. At \(w=.22\) this selects the two cases in
\(\zeta_-(z)\). At \(w=.49\), the real argument lies
strictly between \(1/2\) and one, so the minimum is at
\(\zeta=.068\). At \(z=.28,w=.22\), the original
factor is \(1+R>0\), giving argument zero at every height.
This proves (3). \(\square\)

For the regular two-incidence force, Lemma 1 gives the exact
lower expression
\[
 \begin{split}
 \min_t B(v,t;z,h)
   ={}&A(v+z,e^{2\pi h})-3A(z,e^{2\pi h})\\
      &+\min\{G_-(z,h),G_+(z,h)\}.
 \end{split}                                                  \tag{7}
\]
For the true last row, the corresponding formula is
\[
 \min_t B_{\rm end}(t;z,h)
      =-2A(z,e^{2\pi h})+\min\{G_-(z,h),G_+(z,h)\}.
 \tag{8}
\]
Every radius in (7)--(8) is the same actual
\(e^{2\pi h}\); no incoming or following height has
been optimized independently of its occurrence in the force.
The following *profile* rectangle is minimized as a containing
set, while its finite-source eligibility remains the original
separate hypothesis.

## 2. Application to the credited own-three expressions

In the
[affine-credit reduction](research_mixed_first_attached_affine_neighbor_credit.md),
the force is first bounded at \(h=0\). Its four
\(e,v\) endpoint expressions retain
\[
 \lambda_b\left\{\pi(-1+2z)+
                  \min(G_-(z,0),G_+(z,0))\right\}
 \tag{9}
\]
in place of the following-dependent term \(\lambda_bT(z,t)\).
This follows since \(\lambda_b\ge0\).
The first own-three coordinate may still be reduced to
\(x=\min\{z,.22\}\), because (9) is independent of \(x\).
Thus all following real and height variables have been removed
from that conservative test, with both endpoint branches retained.

For an improved comparison using the actual negative \(b\)
height, one must instead use (7) at
\[
                         h=-\lambda_b(x-.1).
 \tag{10}
\]
The old \(x\)-monotonicity proof applies to its specified
affine-credit lower expression. It is not automatically a
monotonicity theorem for the stronger nonlinear expression (7).

## 3. An exact negative value of the containing-box lower test

Consider the following values in the stated containing
coefficient and target intervals:
\[
 \begin{gathered}
 \alpha=0,\quad x=11/50,\quad z=7/25,\quad
 \lambda_a=0,\quad \lambda_b=3/4,\\
 e=49/100,\quad v=2/5,\quad w=11/50 .
 \end{gathered}                                                \tag{11}
\]
The original upper cutoff at this \(z\) is one.
Thus the neighbor coefficient corresponds to the individually
allowed ordinary height \(c_b=-.09\), and its actual
moving height is \(-.09\).
The first coefficient corresponds to the individually allowed
own-three height \(c_a=0\).
No simultaneous coupled-reference eligibility for this pair
of coefficients is asserted.

At \(w+z=1/2\), its following argument is zero for every
permitted following height. Hence the first endpoint in (9)
is exactly zero. At \(\lambda_a=0\), the original first
derivative is exactly
\[
 P_0=\log\frac{\cos(.21\pi)\cos(.12\pi)}
                            {\sin^2(.22\pi)}.
 \tag{12}
\]
The original chirp is purely imaginary here; no allocation
or real constant has been dropped.
Since \(d=3/25\), \(L(.4)=37/29\), the affine-credit
lower expression for this prescribed following branch is
\[
 \underline{\mathcal H}_0
 =P_0-\frac{3\pi}{10}
        +\frac{37\pi}{29}\frac9{16}\frac3{25}
 =P_0-\frac{2481\pi}{11600}.
 \tag{13}
\]

Here is a purely analytic upper bound on (12).
The alternating Taylor polynomials
\[
 C_4(u)=1-u^2/2+u^4/24,\qquad
 S_7(u)=u-u^3/6+u^5/120-u^7/5040
 \tag{14}
\]
and \(157/50<\pi\) give
\[
 \begin{split}
 \cos(.21\pi)&<C_4(3297/5000)<791/1000,\\
 \cos(.12\pi)&<C_4(471/1250)<93/100,\\
 \sin(.22\pi)&>S_7(1727/2500)>637/1000.
 \end{split}                                                  \tag{15}
\]
These are elementary rational comparisons. For the last one,
at \(u=1727/2500\) a convenient further lower bound is
\[
 u-\frac{(691/1000)^3}{6}
      +\frac{(69/100)^5}{120}
      -\frac{(7/10)^7}{5040}>\frac{637}{1000}.
 \tag{16}
\]
The first two inequalities in (15) may similarly be checked
by using respectively \(659/1000<u<33/50\) and
\(u=471/1250<19/50\) in the quadratic and quartic terms.

It follows that
\[
 \frac{\cos(.21\pi)\cos(.12\pi)}{\sin^2(.22\pi)}
 <\frac{735630}{405769}
 <\frac{9107}{5000}
 <e^{3/5}.
 \tag{17}
\]
The middle strict cross-product difference is \(17188283\).
The last rational is precisely the positive exponential
series through degree four at \(3/5\).
Thus \(P_0<3/5\).
Combining this with \(\pi>3\) in (13) proves
\[
 \boxed{\quad
 \underline{\mathcal H}_0
    <\frac35-\frac{7443}{11600}
    =-\frac{483}{11600}<-\frac1{25}.
 \quad}                                                       \tag{18}
\]
Taking the minimum over the two following branches can only
decrease this lower expression.
No primitive, source, root or numerical proposal was evaluated
to prove (18).

## 4. What the witness does and does not obstruct

Equation (18) shows that a test requiring this particular
affine-credit lower bound to be nonnegative on the entire
independent containing rectangle cannot succeed.
It does not show that the actual coupled derivative is negative,
that this private profile is active in the finite envelope,
or that the reference coefficients in (11) occur simultaneously.
In particular it is not a counterexample to the original
compensated boundary inequality.

The lost term is explicit. At (11), the actual regular
neighbor force for the lower following branch is
\[
 A(.68,r_b)-3A(.28,r_b)+.44\pi,\qquad
                         r_b=e^{-9\pi/50},
 \tag{19}
\]
whereas (13) retains only its affine lower credit.
The earlier proof also retains a stronger, \(z\)-dependent
common-denominator bound before its global minimization.
Consequently an improvement can preserve that dependence,
use (7) with the actual radius, or prove a sharper restriction
on the simultaneous canonical reference coefficients.
No sign of (19) is assumed in this deduction.

The two exact following branches, all original first-cap and
ordinary allocations, both height coefficients and the
relative-pinning terms remain in the source problem.
No complete boundary sign or whole-source lower bound follows
from the present elimination and negative lower-test witness.
