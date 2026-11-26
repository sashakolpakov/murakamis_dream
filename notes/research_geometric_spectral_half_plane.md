# Geometric boundary colors stay in an accretive half-plane

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The positive geometric solution has a useful uniform separation from
the ordinary Jacobi spectrum. This holds throughout the fractional-charge
cube, not only near its complete corner. It gives a uniformly bounded
ordinary Jacobi resolvent at the actual complex geometric boundary
colors. The full normal forcing and the final Fourier observation still
have to be retained; this theorem does not estimate their cancellation.

## 1. Statement and geometric inputs

Take a positive circle-tree path as in the
[fractional-charge theorem](research_positive_path_fractional_charge_cube.md):
the integer powers satisfy \(n_v\ge3\), the charges satisfy
\(0\le\chi_v\le1\), and at least one end is complete. At a
positive-charge vertex write
\[
 t_v=a_v-iH_v,\qquad
 r_{v,e}=k_{v,e}+ig_{v,e}
   =\operatorname{arsinh}\bigl(\tan(t_v/2)\cos(t_w/2)\bigr).
 \tag{1}
\]
All returns have the original positive branch. The already proved
height and sector bounds are
\[
 0<a_v<\pi,\qquad 0<H_v<23/20,\qquad
 B_v:=\frac{\sinh H_v}{\sin a_v}<\sqrt3 .
 \tag{2}
\]
The period equations are
\[
 \sum_{e\ni v} k_{v,e}=\frac{n_vH_v}{2},\qquad
 \sum_{e\ni v} g_{v,e}=\frac{n_va_v}{2}-\pi\chi_v.
 \tag{3}
\]
At a zero charge, \(t_v=0\). Outside complete angles are also zero.

**Theorem 1.** Every spectral boundary color
\(w_v=-2\cos t_v\) on this entire charge cube satisfies
\[
                         \Re w_v<\frac74.
 \tag{4}
\]
The constant is independent of the path length and the powers.
More generally, the same conclusion holds on any finite same-index
network for which (1)--(3) and the stated complete boundary conditions
hold. No new existence or height theorem for such a network is asserted.

## 2. An angle bound from the original returns

Define the decreasing positive function
\[
 m(B)=\frac{\sqrt3-B}{1+\sqrt3 B},\qquad 0<B<\sqrt3.
 \tag{5}
\]
For a neighboring selected angle \(b-ih\), the sector inequality gives
\[
 \tan\arg\cos((b-ih)/2)
   =\tan(b/2)\tanh(h/2)
   =\frac{\sinh h}{\sin b}\frac{1-\cos b}{1+\cosh h}
   <\sqrt3.
 \tag{6}
\]
Thus this argument lies in \([0,\pi/3)\), with value zero at a
complete neighbor. Meanwhile
\(\arg\tan((a-iH)/2)=-\arctan B\). Their product has positive
real part. If its argument \(\varphi\) is positive, then
\(\tan\varphi\le m(B)\). For its return \(r=k+ig\),
\[
 \tan g=\tan\varphi\tanh k,
 \qquad 0<g<\pi/2,
 \qquad g\le k\tan\varphi\le k m(B).
 \tag{7}
\]
Here \(k>0\). When \(\varphi\le0\), also \(g\le0\), so the
last inequality in (7) remains valid. Summing (7), and using (3),
proves
\[
                   a-\frac{2\pi}{3}\le Hm(B),
              \qquad B=\frac{\sinh H}{\sin a}.
 \tag{8}
\]
This deduction uses \(2\pi\chi/n\le2\pi/3\), and does not use
the number of incident edges.

There is a useful first consequence:
\[
 Hm(B)\le \sin a\,B m(B)\le\frac{\sin a}{3},
 \qquad a\le\frac{2\pi}{3}+\frac13.
 \tag{9}
\]
Indeed \(H\le\sinh H\). Differentiation shows that
\(B m(B)\) has its unique maximum \(1/3\) at \(B=1/\sqrt3\).

## 3. A uniform separation from the line \(\Re w=2\)

Since \(\Re w=-2\cos a\cosh H\), the assertion is immediate
when \(a\le\pi/2\). We henceforth suppose \(a>\pi/2\).
Put
\[
 H_c=\operatorname{arcosh}\sqrt3,\qquad
 a_0(H)=\arccos(-\operatorname{sech}H),\qquad
 D(a,H)=a-\frac{2\pi}{3}-H m\!\left(\frac{\sinh H}{\sin a}\right).
 \tag{10}
\]
The angle \(a_0(H)\) is exactly where \(\Re w=2\), and (8)
says \(D(a,H)\le0\). On the sector where
\(\pi/2<a<\pi\) and \(B\le\sqrt3\),
\[
 1<\partial_aD
   =1+\frac{4HB(-\cot a)}{(1+\sqrt3B)^2}
   \le1+\frac{4B^2}{(1+\sqrt3B)^2}\le\frac74.
 \tag{11}
\]
The middle inequality uses \(H/\sinh H\le1\) and
\(|\cos a|\le1\). In particular the sector interval has a
uniform derivative bound even near an angle endpoint.

We use four elementary ranges of \(H\).

**Small heights: \(0<H\le1/2\).** From (9) and
\(\cos(2\pi/3+x)\ge-1/2-\sqrt3 x/2\),
\[
 \cos a>-\frac{19}{24},\qquad \cosh H<\frac87,
 \qquad \Re w<\frac{38}{21}<2-\frac1{3500}.
 \tag{12}
\]

**Intermediate heights: \(1/2\le H\le1\).** We have
\(\cosh1<8/5\), and
\[
 \arccos(-5/8)>\frac{2\pi}{3}+\frac{2}{15}.
 \tag{13}
\]
For (13), the cosine at the right side is greater than
\(-1/2-(7/4)/15=-37/60>-5/8\).
Since \(a_0(H)\) decreases in \(H\), (13) is a lower bound
for \(a_0(H)\). Also \(\sqrt3<7/4\), \(\sqrt3>5/3\), and
\(\cosh H\ge1+H^2/2\) give
\[
 Hm(\cosh H)
 \le\frac38\left(\frac{3H}{4}-\frac{H^3}{2}\right)
 \le\frac{3}{16\sqrt2}.
 \tag{14}
\]
Consequently
\[
 D(a_0(H),H)>
       \frac{2}{15}-\frac{3}{16\sqrt2}>\frac1{2000}.
 \tag{15}
\]
At \(a=a_0(H)\) the sector ratio is \(B=\cosh H<\sqrt3\).
Monotonicity in (11) first implies \(a<a_0(H)\). The whole
interval between these angles remains in the sector. Using its
upper derivative bound then gives
\[
 a_0(H)-a>\frac1{3500},\qquad
 2-\Re w
   \ge2\sinh H\,(a_0(H)-a)>\frac1{3500}.
 \tag{16}
\]
For the second inequality, integrate sine between the two angles;
on \([\pi/2,a_0]\) it is at least \(\sin a_0=\tanh H\).

**Higher heights: \(1\le H\le H_c\).** The elementary bounds
\(H_c<6/5\), \(\cosh1>3/2\), and the preceding bounds on
\(\sqrt3\) imply
\[
 Hm(\cosh H)<\frac3{35}.
 \tag{17}
\]
On the other hand
\[
 a_0(H)\ge\arccos(-1/\sqrt3)
       >\frac{2\pi}{3}+\frac3{35}+\frac1{1000}.
 \tag{18}
\]
For the strict inequality use the same cosine estimate: at the
right side its value is greater than
\(-32249/56000>-1/\sqrt3\), since
\(3\cdot32249^2<56000^2\).
Thus \(D(a_0,H)>1/1000\). The argument proving (16) gives the
stronger gap \(2-\Re w>1/875\).

**The remaining heights: \(H_c\le H<23/20\).** If
\(a\le2\pi/3\), then \(\Re w\le\cosh H<7/4\).
Otherwise \(\sin a<\sqrt3/2\) and
\[
 B>2\sqrt{2/3}>8/5,
 \qquad m(B)<9/220,
 \qquad a<\frac{2\pi}{3}+\frac{207}{4400}.
 \tag{19}
\]
Here (8) and \(H<23/20\) give the last inequality.
The cosine bound and \(\cosh(23/20)<7/4\) now imply
\[
 \Re w<\frac{133343}{70400}<\frac{19}{10}
                            <2-\frac1{3500}.
 \tag{20}
\]
This proves the preliminary bound \(\Re w_v<2-1/3500\).
Zero-charge vertices have \(w=-2\), so it includes every face
of the cube. The next step improves this bound to (4).

All numerical constants in this proof are certified by elementary
rational comparisons. For example, for \(0\le x\le23/20\),
\[
 \cosh x\le1+\frac{x^2}{2}
       +\frac{x^4}{24(1-x^2/30)}.
 \tag{21}
\]
This follows by bounding the ratios of the remaining even Taylor
terms by \(x^2/30\). It proves each upper bound on \(\cosh\)
used above. The fourth-degree Taylor lower bound proves
\(\cosh(6/5)>7/4>\sqrt3\).

## 4. Improving the return angle bound

The preliminary bound implies \(\Re w_v<2\) at every vertex.
Since \(w_v=-2\cos t_v\),
\[
 \Re\bigl(\cos^2(t_v/2)\bigr)
                =\frac{1+\Re\cos t_v}{2}>0.
 \tag{21a}
\]
The real part of \(\cos(t_v/2)\) is positive and its imaginary
part is nonnegative. Therefore
\(0\le\arg\cos(t_v/2)<\pi/4\). We may now repeat the return
argument with \(\pi/4\) in place of \(\pi/3\).

If \(B\ge1\), all return imaginary parts are nonpositive,
and (3) gives \(a\le2\pi/3\). If \(B<1\), the new estimate is
\[
 a-\frac{2\pi}{3}
  \le H\frac{1-B}{1+B}
  \le\sin a\,\frac{B(1-B)}{1+B}
  \le(3-2\sqrt2)\sin a<\frac{\sin a}{5}.
 \tag{21b}
\]
The maximum occurs at \(B=\sqrt2-1\), and
\(\sqrt2>7/5\) gives its strict upper bound \(1/5\).

For \(a\le2\pi/3\), the original height bound already gives
\(\Re w\le\cosh H<7/4\). Otherwise (21b) implies
\(a<2\pi/3+\sqrt3/10\), hence \(\cos a>-13/20\).
In this case \(B<1\) also gives
\(\sinh H<\sin a<\sqrt3/2\). Consequently
\[
 \cosh H<\frac{\sqrt7}{2}<\frac43,
 \qquad \Re w<\frac{26}{15}<\frac74.
 \tag{21c}
\]
This proves Theorem 1. The improvement uses the preliminary bound
at all neighboring vertices, so there is no assumption of the
stronger angle sector in its first proof.

## 5. The ordinary Jacobi resolvent at the geometric point

Let \(c_0=2\cos(\pi/N)\), and let \(J_j\) be any ordinary
physical Jacobi truncation appearing in the
[normal formula](research_all_color_path_normal_bound.md#5-the-complete-normal-determinant-at-every-color-assignment).
Its established Dirichlet form gives \(J_j\ge c_0I\).
For \(N\ge16\), (4) and \(\pi^2<10\) give
\[
 c_0-\Re w_v>
    \frac14-\frac{\pi^2}{N^2}
    >\frac15.
 \tag{22}
\]
Thus, uniformly in the level, row, path, powers, and charge vector,
\[
 \Re\langle x,(J_j-w_vI)x\rangle\ge
        \frac15\|x\|^2,
 \qquad \|(J_j-w_vI)^{-1}\|\le5 .
 \tag{23}
\]
This is an estimate at the actual complex geometric colors. It does
not replace the endpoint normal polynomial \(Q(w)\) or the full
free-boundary term \(P_N(w)\) in the original normal identity.
Those terms need their own estimates on any complex contour.
Likewise, an accretive ordinary-value problem does not prove that
its final signed Fourier observation has a nonzero geometric
coefficient.

The [rational checker](../experiments/verify_geometric_spectral_half_plane.py)
verifies the numerical comparisons used above without floating-point
root searches. Its [record](../repro/results/research-geometric-spectral-half-plane.json)
checks the constants only; the all-path assertion follows from the
return inequality and the four written angle estimates.
