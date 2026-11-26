# Directional central costs at the second selection

Research deduction, 6 November 2026. The two Fourier rates arise from
an additive estimate for the original polynomial; they cannot be
replaced by their minimum. Their domains can, however, be restricted
according to which rate dominates. A joint horizontal Hessian estimate
then reduces the central comparison to three scalar gains, with no
nonconvex separated-edge conjugates or trial-flow search. The resulting
uniform signs are not proved here. No source or numerical evaluation
is performed.

## 1. What the two Fourier alternatives mean

Retain the exact polynomial \(d_N\), the reciprocal-factorial
continuation \(f_N\), and \(X=e^{-2\pi iz}\) from
[the Fourier continuation proof](research_mixed_fourier_weight_continuation.md).
Its equations (8), (17), and (19) give an exact identity and estimates
of the form
\[
 \begin{split}
 d_N(X)&=f_N(z)+(1-X^N)I_N(z),\\
 |f_N(z)|&\le N^C e^{-N\Re g(z)},\\
 |(1-X^N)I_N(z)|&\le C_\tau N^C
                   e^{N(2\pi(\Im z)_++\tau)}.
 \end{split}
 \tag{1}
\]
All four original residue-contour sides occur in \(I_N\). In
particular it is not set to zero when the interpolation agrees on
the physical root grid. At a positive selected height \(H\), multiply
by the literal \(X^{-N}\). Equation (1) gives
\[
 |d_N(X)X^{-N}|
 \le C_\tau N^C\left\{
          e^{N(-\Re g(z)-2\pi H+\tau)}+e^{N\tau}\right\}.
 \tag{2}
\]
Thus the two rate functions are
\[
            w_H(x)=-\Re g(x+iH)-2\pi H,\qquad 0.
 \tag{3}
\]
This is a sum upper bound, and hence a maximum at exponential scale,
not two separate upper bounds whose minimum is available. The bound
does not assert a nonzero leading remainder at every point; proving
additional cancellation or a better remainder would require another
argument. The relative factorial theorem already available applies
where \(w_H\) has a strictly positive margin, rather than to every
point of the selected plateau.

Now fix \(H=1/100\), as in the
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md),
and \(P=[11/50,9/20]\).

**Lemma 1 (the rate switch).** There is a unique
\[
                   x_H\in(2/5,9/20)
       \quad\text{such that}\quad w_H(x_H)=0.
 \tag{4}
\]
The factorial rate dominates on \(x\le x_H\), and the forced
rate dominates on \(x\ge x_H\).

*Proof.* With \(R=e^{2\pi H}>1\),
\[
 w_H'(x)=-\log|1-Re^{-2\pi ix}|<0,\qquad x\in P.
 \tag{5}
\]
Indeed \(\cos(2\pi x)\le\cos(.44\pi)<1/5\), so
\(|1-Re^{-2\pi ix}|^2>1+R^2-2R/5>1\).
At \(x=2/5\), the original argument
\(\arg(1-e^{2\pi k-4\pi i/5})\) is positive for
\(0\le k\le H\). Since it is the height derivative of
\(-\Re g\), the real-axis integral gives
\[
 w_H(2/5)\ge\frac1{10}\log(2\sin(2\pi/5))
                         -\frac{\pi}{50}>\frac1{875}>0.
 \tag{5a}
\]
Here \(\sin^2(2\pi/5)=(5+\sqrt5)/8>(19/20)^2\),
using \(\sqrt5>111/50\), and
\(\log(19/10)>16/25\). For an explicit rational witness
to the latter, at \(t=16/25\) the positive exponential series gives
\[
 e^t\le \sum_{j=0}^5\frac{t^j}{j!}
               +\frac{t^6}{6!(1-t/7)}
 =\frac{132512906251}{69873046875}<\frac{19}{10},
 \quad
 \frac{19}{10}-\frac{132512906251}{69873046875}
 =\frac{491765623}{139746093750}>0.
 \tag{5b}
\]
Now use \(\pi<22/7\) in (5a).
At the other endpoint, write \(J(t)=\Re g(t)\) on the real
interval. Then \(J(1/2)=0\) and
\(J'(t)=\log(2\sin\pi t)<\log2\) give
\[
 -J(9/20)<\frac{\log2}{20}.
 \tag{6}
\]
For \(0\le k\le H\), the original argument
\(\arg(1-e^{2\pi k-.9\pi i})\) lies in \((0,\pi/10)\).
It is the derivative in \(k\) of \(-\Re g(9/20+ik)\).
Consequently
\[
 w_H(9/20)<
       \frac{\log2}{20}-\frac{19\pi}{1000}<0,
 \tag{7}
\]
using \(\log2<7/10\) and \(\pi>3\).
Strict monotonicity and continuity prove the assertion. \(\square\)

This yields an exact reduction of the upper-rate envelope:
the factorial objective need only be bounded on
\(I_1=[11/50,x_H]\), and the forced objective only on
\(I_0=[x_H,9/20]\). A simpler conservative choice, requiring
no evaluation of \(x_H\), is
\[
              \widetilde I_1=P,\qquad
              \widetilde I_0=[2/5,9/20].
 \tag{8}
\]
These restrictions concern the common selected coordinate in the
entire profile objective. They leave every ordinary index and both
retained boundary coordinates free. No minimum of the Fourier rates
is used.

## 2. Actual reference, gradients, and the justified product

Use the notation and exact trial data of the
[central main/main budget](research_mixed_second_selected_central_budget.md):
\[
 \begin{gathered}
 (a,u,z,v,b)=(r_1,s_2,r_2,s_3,r_3),\qquad
 (\epsilon_1,\epsilon_2,\epsilon_3)=(\alpha,1,\beta),\\
 m\ge4,\quad \alpha,\beta\in\{0,1\},\quad z_*=x_*+ic,\quad c<0.
 \end{gathered}
 \tag{9}
\]
Position 1 is unselected. Only the height of \(z\) changes to
\(H\); all other heights remain actual. In particular \(a\)
is the actual attached first output and \(u,v,b\) are ordinary
coordinates, also at length four.

Let \(f_\nu\), \(M\), \(T_\nu\), \(A,B,C,\ell,D_\nu\)
be exactly equations (4)--(9) of that budget, with
\(\nu=1\) factorial and \(\nu=0\) forced. The two original
boundary marginals remain subtracted. At the real reference, evaluated
at final selected height,
\[
 f_\nu(x_*)-M=T_\nu,\qquad
 \nabla f_\nu(x_*)=(0,A,D_\nu,-d,0),\qquad d=\ell-B>0,\ A>0.
 \tag{10}
\]
The exact logarithmic formulas for these quantities and the vertical
trial cost are unchanged. In particular the \(-\ell\) in
the right index derivative is the original incoming chirp. The
actual references satisfy \(x_*\in(.24,.36)\).

The [index-barrier and concavity theorem](research_mixed_second_selected_horizontal_concavity.md)
reduces both maxima on the original product to
\[
 K'=P\times[.22,.5]\times P\times[q_\beta,.5]\times P,
 \qquad q_0=.2,\quad q_1=.22.
 \tag{11}
\]
The barriers are pointwise in the other variables, so remain valid
after either selected-coordinate restriction in (4) or (8).
Even when \(x_*\) is outside a restricted selected interval,
the full connecting segment from the actual real trial stays in
the original \(K'\). It is this larger connecting domain that
will be used in the Hessian argument.

## 3. A directional joint cost with zero boundary optimizations

Write \(g_h(t)=\Re g(t+ih)\). Let
\[
 \begin{split}
 \phi_u(t)&=g_{h_u}(u_{*,R}+t)-g_{h_u}(u_{*,R})
                          -g_{h_u}'(u_{*,R})t,\\
 \phi_{z,\nu}(t)&=(1+\nu)\{
       g_H(x_*+t)-g_H(x_*)-g_H'(x_*)t\},\\
 \phi_v(t)&=g_{h_v}(v_{*,R}+t)-g_{h_v}(v_{*,R})
                          -g_{h_v}'(v_{*,R})t.
 \end{split}
 \tag{12}
\]
These costs use their true real centers and final heights.
For \(\beta=0\), put
\[
 \delta_v=\min\{\Re\cot(\pi v_*),15/53\}>1/5,\qquad
 \kappa_0=2\pi\delta_v,
 \qquad \kappa_1=39\pi/80.
 \tag{13}
\]
The simpler choice \(\kappa_0=2\pi/5\) is also valid.
Define on the full right-index displacement interval
\[
 \Psi_\beta(t)=\beta\phi_v(t)
                   +\frac{\kappa_\beta}{2}\min(t,0)^2.
 \tag{14}
\]
This is convex and continuously differentiable, with value and first
derivative zero at the actual center.

**Proposition 2 (joint directional majorant).** For every target
in \(K'\), with displacements
\((t_a,t_u,t_z,t_v,t_b)\) from the actual real trial,
\[
 f_\nu-M\le
 T_\nu+A t_u+D_\nu t_z-dt_v
                -\phi_u(t_u)-\phi_{z,\nu}(t_z)-\Psi_\beta(t_v).
 \tag{15}
\]
The incoming and outgoing targets remain unrestricted in \(P\);
they have not been fixed to their reference values.

*Proof.* Equations (19)--(21) of the concavity theorem are simultaneous
matrix bounds. On all \(K'\), their diagonal cost includes
\[
 \frac{1+\alpha}{2}g_{h_a}'',\quad
 g_{h_u}'',\quad(1+\nu)g_H'',\quad
 \beta g_{h_v}'',\quad\frac{1+\beta}{2}g_{h_b}''.
 \tag{16}
\]
When \(v_R\le v_{*,R}\), each of the two right pairs supplies
the additional index curvature \(\pi\delta_v\) for
\(\beta=0\), or \(39\pi/160\) for \(\beta=1\).
The latter is in addition to the own index factorial already
retained in (16). The stronger type-three comparison uses the fixed
height \(h_v=\Im v_*\); this hypothesis holds along every
present segment.

For a target with negative \(t_v\), every interior point of its
straight connecting segment lies on the stronger side of that
reference face. For a target with nonnegative \(t_v\), use
only (16). Integrating the appropriate joint matrix inequality
therefore gives (14), together with the scalar Bregman costs in
(12) and the two nonnegative boundary costs from (16).
Both boundary forces in (10) vanish, so those last two costs
may be discarded. Equation (10) now proves (15).
No optimizer direction, active face, or decoupling of the original
reference is assumed. \(\square\)

## 4. Three gains and their clipping rules

For either interval choice \(I_\nu\) in Section 1 define
\[
 \begin{split}
 \mathcal U(A)
   &=\max_{0\le t\le .5-u_{*,R}}\{At-\phi_u(t)\},\\
 \mathcal R_\beta(d)
   &=\max_{0\le t\le v_{*,R}-q_\beta}
       \{dt-\beta\phi_v(-t)-\kappa_\beta t^2/2\},\\
 \mathcal Z_\nu(D;I_\nu)
   &=\max_{x_*+t\in I_\nu}
                       \{Dt-\phi_{z,\nu}(t)\}.
 \end{split}
 \tag{17}
\]
Because \(A>0\), the left-index scalar objective is nonpositive
for a negative displacement, whereas zero displacement is available.
Because \(d>0\), the right-index scalar objective is nonpositive
for a positive displacement. Thus (17) is exactly the supremum
of the three separated terms in (15), not a guess about the
maximizer of the original coupled function.

The selected-coordinate gain in (17) must retain its actual signed
value. For the forced branch the reference \(x_*<.36\)
is outside both allowed intervals \(I_0\) from Section 1.
Consequently \(\mathcal Z_0\) can be negative. Replacing it
by a zero-force convention or silently adding the unavailable
center would discard a legitimate favorable cost.

**Theorem 3 (three-scalar central budget).** The main/main upper-rate
envelope satisfies
\[
 \max_{x\in K'}\max_{\nu=0,1}(f_\nu(x)-M)
 \le
 \max_{\nu=0,1}
 \{T_\nu+\mathcal U(A)+\mathcal R_\beta(d)
                       +\mathcal Z_\nu(D_\nu;I_\nu)\}.
 \tag{18}
\]
This holds with the exact switched intervals (4), or with the
conservative intervals (8). All quantities on the right belong
to one original reference.

*Proof.* Equation (3) gives \(f_1-f_0=w_H(z_R)\).
The exact intervals retain the dominating branch pointwise, so
their two restricted maxima give the original maximum exactly.
Enlarging those intervals as in (8) preserves an upper bound.
Apply (15) and (17) to each restricted maximum. \(\square\)

Here every scalar gain is monotone-concave optimization in one
variable, with at most one critical point. More explicitly, set
\[
 N_h(x)=1+e^{4\pi h}-2e^{2\pi h}\cos(2\pi x),
 \qquad
 {\cal T}(q)=\frac{\arccos(\operatorname{clip}(q,-1,1))}{2\pi}.
 \tag{19}
\]
For a potential \(m g_h\), force \(p\), and true center \(x_0\),
the unconstrained critical real target is
\[
 {\cal T}\left(
   \frac{1+e^{4\pi h}-N_h(x_0)e^{2p/m}}{2e^{2\pi h}}\right).
 \tag{20}
\]
Clip this target to \([u_{*,R},.5]\) for \(\mathcal U\),
with \(m=1,p=A,h=h_u\), or to \(I_\nu\) for
\(\mathcal Z_\nu\), with \(m=1+\nu,p=D_\nu,h=H\).
Always evaluate the original objective at the clipped target;
the true center in (12) and (20) is never clipped.

For \(\beta=0\), let
\[
 t_0=\min\{d/\kappa_0,v_{*,R}-.2\},\qquad
             \mathcal R_0(d)=dt_0-\kappa_0t_0^2/2.
 \tag{21}
\]
For \(\beta=1\), its critical displacement is the unique
nonnegative solution, with endpoint clipping, of
\[
 d=g_{h_v}'(v_{*,R})-g_{h_v}'(v_{*,R}-t)+\kappa_1t.
 \tag{22}
\]
The right side is strictly increasing from zero on the permitted
interval. A simpler proven upper replacement is
\[
 \mathcal R_1(d)\le
 \max_{0\le t\le v_{*,R}-.22}
                   \{dt-(71\pi/160)t^2\}.
 \tag{23}
\]
Indeed \(g_{h_v}''>2\pi/5\) on this downward segment,
and \(2/5+39/80=71/80\). No scalar equation in
(20)--(22) is a source critical-root reconstruction.

This budget removes the four potentially nonconvex edge conjugates
and every trial-flow choice from the earlier scalar relaxation.
It is an alternative majorant obtained by a proved joint Hessian
allocation, rather than a claimed pointwise improvement over every
choice in the exact pair dual. One may take the minimum of valid
upper bounds for the same branch and domain; one may not take
the minimum of the two distinct Fourier rates in (2).

Uniform negativity of (18) remains an actual-reference inequality.
The exact vertical trial cost, both boundary tangents, and the
coupled two-transfer reference are still essential. The deduction
alone proves neither the main/main gap nor the whole finite-source
second-selection theorem.
