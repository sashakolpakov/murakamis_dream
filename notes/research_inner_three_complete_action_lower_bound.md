# A rational lower bound for the original complete three-action

Private written deduction, 9 November 2026. No mathematical numerical
evaluation, saved-value arithmetic, or frozen-source edit is used.

The original calibrated complete action satisfies
\[
                         \boxed{M_3>\frac{46}{25}>\frac{11}{6}.}
\tag{1}
\]
This is an action comparison. It supplies no new finite-kernel domain
or signed-observation estimate.

## 1. Source and normalization

Keep the full canonical source
\[
 P_{3,N}(u,v)=\phi_N^{(t)}
       [R^3K_N(t,u)K_N(t,v)]
\]
of [the full single-vertex theorem](research_all_nonzero_degree_two_fillings.md),
with both boundary polynomials and every repeated-root normal retained.
Its selected phase at completeness is the stationary value of
\[
 \Phi(t,0)=2\psi(t,0)+\frac{3it^2}{4\pi}-it,
 \qquad
 M_3=\Re S_3(0,0)=\Re\Phi(t_3,0).
\tag{2}
\]
The [original cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
identifies this same logarithmic branch and complete constant, and gives
\[
 t_3=a_3-iH_3,\qquad
              0<a_3<\pi/2,\qquad0<H_3<1.
\tag{3}
\]
The [complete-action upper-bound proof, Section 1](research_inner_three_complete_action_upper_bound.md)
also proves \(H_3>2/3\) directly from this original cubic.
For clarity, its distinguished root \(v=2\cos(t_3/2)=x+ib\) has
\(x>3/2\), \(1/3<b<2/3\), and
\[
 (3b-2)x^2-b^3+2b^2-3b+2=0.
\]
The left side increases with \(b\) on that interval and is negative
at \(b=1/2\), so \(b>1/2\). But if \(H_3\le2/3\), then
\[
 b=2\sin(a_3/2)\sinh(H_3/2)
 <\sqrt2\,\sinh(1/3)
 <\frac{10}{7}\frac{18}{53}
 =\frac{180}{371}<\frac12,
\]
a contradiction. Here \(\sinh(1/3)<18/53\) follows by bounding
successive positive series-term ratios by \(1/54\).
In particular no factor of two is inserted in the definition of \(M_3\).
The modulus-one scalar \(C_{N,3}\) of the full source is unchanged.

The original complete-edge primitive is
\[
 \psi(t,0)=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi)),
 \quad J'(z)=\Log(2\sin\pi z),\quad J(0)=0.
\tag{4}
\]
Its arguments remain in their original regular strips on the rectangle
used below.

## 2. A fixed real-part comparison

The [positive horizontal phase theorem, equation (26)](research_mixed_next_inner_three_positive_horizontal_phase_extension.md)
compares the original saddle with every point of its positive
horizontal, in particular with \(t=\pi/2-iH_3\). Thus
\[
 M_3\ge\Re\Phi(\pi/2-iH_3,0)
       =2\Re\psi(\pi/2-iH_3,0)-\frac{H_3}{4}.
\tag{5}
\]
Only this phase comparison is used; no finite source is moved to that
point in the present argument.

The [complete-edge gap proof, equations (12)--(14)](research_internal_pair_complete_edge_gap.md)
establishes, on \(0\le H\le107/100\), the exact inequalities
\[
 \psi(\pi/2,0)>\frac{239}{250},\qquad
 \Re\psi(\pi/2-iH,0)
 \ge\psi(\pi/2,0)+
                \frac{H^2/2-H^4/24}{\sqrt2\,\pi}.
\tag{6}
\]
These are bounds for (4), including its complete constant. Their
written proof uses the first three positive blocks of the integrated
Fourier series for the real value, and
\[
 \Im\operatorname{arsinh}\tan((\pi/2-iH)/2)
       =-\arctan(\sqrt2\sinh(H/2))
\]
for the height correction. Monotonicity of arctangent and
\(\arctan x\ge x-x^3/3\) give the correction in (6).
We use these established inequalities literally, without rerunning
their scalar check or calculating from its saved record.

Equations (5)--(6) imply
\[
 M_3>\frac{239}{125}
           +\frac{H_3^2-H_3^4/12}{\sqrt2\,\pi}-\frac{H_3}{4}.
\tag{7}
\]
Let \(f(H)=(H^2-H^4/12)/(\sqrt2\,\pi)-H/4\).
The polynomial \(2H-H^3/3\) increases on \([2/3,1]\).
Using \(\sqrt2<10/7\), \(\pi<22/7\), one obtains throughout
that interval
\[
 f'(H)=\frac{2H-H^3/3}{\sqrt2\,\pi}-\frac14
       >\frac{100}{81}\frac{49}{220}-\frac14
       =\frac{245}{891}-\frac14>0.
\tag{8}
\]
The actual height is in this interval. Therefore
\[
 M_3>\frac{239}{125}+f(2/3)
       >\frac{239}{125}-\frac16
                         +\frac{104}{243}\frac{49}{220}
       =\frac{239}{125}-\frac16+\frac{1274}{13365}
       >\frac{46}{25}.
\tag{9}
\]
For the final strict comparison,
\(46/25-239/125+1/6=71/750\), and the positive
cross-product difference is
\[
           1274\cdot750-71\cdot13365=955500-948915>0.
\]
Finally \(46/25-11/6=1/150>0\). This proves (1).

## 3. Frozen inputs and scope

The source files used above have SHA-256 hashes:

| Source | SHA-256 |
|---|---|
| Full single-vertex theorem | 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c |
| Original cubic continuation | 8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a |
| Complete-action upper-bound proof | 7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d |
| Positive horizontal phase theorem | a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c |
| Complete-edge gap proof | 1ac5e324eeb4f11425b6937332e08a682c802ce3d1fb3b6646cf7ecffed38ac3 |

The conclusion concerns exactly \(M_3=\Re S_3(0,0)\) of the original
full canonical source, through either level parity. It does not change
the action, its scalar convention, or any source-domain limitation.
No claim about a completed attachment budget or finite exceptions
follows from this lower bound alone.
