# The retained three-crossing packet on a real input interval and an output union

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original finite retained kernel has a larger useful domain when the
input displacement is real. Separate contours on eight real-input
intervals avoid the unnecessary opposite-height sides of one large
symmetric index rectangle. The conclusion is a source asymptotic; it
does not assert a new cap entrance or a complete-chain lower bound.

## 1. Source and statement

Set
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 I=\{x_h+a:|a|\le1/50\},\qquad
 U=\{|y-x_h|\le1/200\}\ \cup\
       \{x_h+b:b\in\mathbb R, |b|\le9/1000\}.
 \tag{1}
\]
The source is precisely the L40 source of the
[genuine bidisk theorem](research_three_vertex_bidisk_packet.md):
\[
 L=\lfloor N/40\rfloor,\qquad
 E_L=M^TP_LJMP_LM,\qquad
 \widetilde V_N^{(40)}(x,y)=h(x)^T(JM^3-E_L)h(y).
 \tag{2}
\]
In its exact root-product sum, the square \(i,j\le L\) is omitted
and every other finite row is retained. In particular this proof
does not modify the original physical first normals or replace
the source by its critical phase.

**Theorem 1.** On a fixed open neighborhood of \(I\times U\),
at both level parities,
\[
 \widetilde V_N^{(40)}(x,y)
   =\kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}(1+O(N^{-1})).
 \tag{3}
\]
The phase and nonzero holomorphic amplitude are exactly the branches
in the bidisk theorem. The normalized error is holomorphic and
uniformly \(O(N^{-1})\), including all fixed parameter derivatives
on a smaller neighborhood. The output disk in (1) is a true complex
disk; no claim for the larger output coordinate square is needed.

## 2. Exact parameter coverage and index contours

Use the original negative-frequency phase
\[
 \begin{split}
 F(s,t;X,Y)={}&s\log X+t\log Y\\
 &+\frac{\operatorname{Li}_2(e^{-2\pi i(s+t)})-\pi^2/6
 -\operatorname{Li}_2(Xe^{-2\pi is})+\operatorname{Li}_2(X)
 -\operatorname{Li}_2(Ye^{-2\pi it})+\operatorname{Li}_2(Y)}{2\pi i},
 \qquad X=e^{2\pi ix},\quad Y=e^{2\pi iy}.
 \end{split}
 \tag{4}
\]
Its continued branch is the one in the bidisk and
[input-rectangle](research_three_vertex_input_rectangle.md) proofs.
Put
\[
 \alpha=X^{-1}-1,\quad\beta=Y^{-1}-1,\quad
 \Delta=1-2(\alpha+\beta)+(\alpha-\beta)^2,
 \quad
 U_c=\frac{1+\alpha-\beta-\sqrt\Delta}{2},\quad
 V_c=\frac{1-\alpha+\beta-\sqrt\Delta}{2},
 \quad(s_c,t_c)=\frac{i}{2\pi}(\log U_c,\log V_c).
 \tag{5}
\]
One outward branch domain covers real input \(|a|\le.02\) and
the entire auxiliary output rectangle
\(|\Re(y-x_h)|\le.009,|\Im(y-x_h)|\le.005\).
It proves \(\Im\Delta>0\), that \(U_c,V_c\) are lower left,
\(\Re X,\Im X,\Re Y,\Im Y>2/25\), \(|X|,|Y|<27/50\), and
\(3/10<\Re s_c,\Re t_c<2/5\),
\(|\Im s_c|,|\Im t_c|<1/25\).
Thus the selected branches are holomorphic in the output disk,
with their original lifts fixed by the connected domain and the
homogeneous point. This auxiliary rectangle is used only for
branch selection, not for the finite contour estimates.

For \(j=0,\ldots,7\), take the real input patch
\[
 (j-4)/200\le a\le(j-3)/200,
 \qquad B=[23/100,9/20].
 \tag{6}
\]
The two index rectangles have real interval \(B\) and the imaginary
endpoints in the following table, in units of \(1/1000\).

| \(j\) | disk: \(s_-,s_+,t_-,t_+\) | real interval: \(s_-,s_+,t_-,t_+\) |
|---:|:---|:---|
| 0 | \(-26,6,-6,23\) | \(-29,6,-6,25\) |
| 1 | \(-20,6,-6,19\) | \(-23,6,-6,21\) |
| 2 | \(-15,6,-6,15\) | \(-18,6,-7,18\) |
| 3 | \(-10,6,-8,12\) | \(-13,8,-11,14\) |
| 4 | \(-6,10,-12,8\) | \(-8,13,-14,10\) |
| 5 | \(-6,15,-15,6\) | \(-6,18,-18,7\) |
| 6 | \(-6,20,-19,6\) | \(-6,23,-22,6\) |
| 7 | \(-6,24,-23,6\) | \(-6,27,-25,6\) |

The disk-output checks use its complete circle
\(y=x_h+e^{2\pi iq}/200\), \(0\le q\le1\), while the
real-output checks use \(y=x_h+(9/500)(q-1/2)\).
The real input varies over the whole patch, never just its endpoints.
For fixed input and fixed indices, the real part of \(F_c-F\),
where \(F_c=F(s_c,t_c;X,Y)\), is harmonic in the output disk.
Consequently its boundary inequalities extend to the full disk.
The same principle applied to \(\Im s_c,\Im t_c\) extends the
certified strict containment in the index rectangles. The contours
are fixed on each input patch, so this reduction introduces no
parameter-dependent index boundary.

For each patch and each output family the certificate proves
\[
 \Re F_c>-1/10,\qquad
 s_-+10^{-5}<\Im s_c<s_+-10^{-5},\qquad
 t_-+10^{-5}<\Im t_c<t_+-10^{-5}.
 \tag{7}
\]
Here the table entries in (7) are divided by 1000. With both
orders of the indices checked separately, its real complement
domains are
\[
 \begin{split}
 &0\le s\le1/40,\quad 1/40\le t,\quad s+t\le99/100,\\
 &1/40\le s\le23/100,\quad 0\le t,\quad s+t\le99/100,\\
 &s=9/20,\quad 0\le t\le54/100.
 \end{split}
 \tag{8}
\]
On these, \(\Re(F_c-F)>1/250\). On all twelve products of
index sides containing a vertical side, it proves
\(\Re(F_c-F)>1/1000\). On all four horizontal-side products,
it proves \(\Re(F-F_c)<1/50\).

The exact cover has 369 domains: one branch domain and, for each
of sixteen patch/family pairs, one floor-and-containment domain,
six ordered real complement domains, and sixteen side products.
There are 15,156 accepted rational boxes. Each acceptance uses an
outward interval enclosure or an outward center value plus a
full-box first-derivative mean-value bound. The circle map and its
derivative are evaluated as complex balls on the full rational
arc interval. No sampled value is used for acceptance.

## 3. Concavity and all finite currents

The exact index Hessian is
\[
 -\Re d^2_{s,t}F=a(ds+dt)^2+d_xds^2+d_ydt^2.
 \tag{9}
\]
Over all the present rectangles, each denominator-angle argument
lies in \([13\pi/150,91\pi/150]\), and its absolute height argument
is at most \(\log2+68\pi/1000\). Since
\[
 \cosh(\log2+68\pi/1000)<3/2,\qquad
 \frac{\pi\sin\theta}{3/2-\cos\theta}>3/2
 \quad(13\pi/150\le\theta\le91\pi/150),
 \tag{10}
\]
we have \(d_x,d_y>3/2\). The middle expression has a single
interior critical point, a maximum, so its two endpoints suffice.
For \(\Re(s+t)\ge1/2\), \(a\ge0\); otherwise
\[
 |a|\le\pi\tan(\pi/25)<2/5,
 \qquad -\Re F''_{s,t}\succ\frac7{10}I_2.
 \tag{11}
\]
The latter follows from \((ds+dt)^2\le2(ds^2+dt^2)\).
This is an index-only estimate at fixed wire parameters, not an
extension of the older joint real-coordinate chamber.

The high real-index strips reduce to the last face in (8).
For \(9/20\le s\le89/100\), the present input and output ranges
give \(1/4<s-\Re x<3/4\), so the original root-product ratio
has denominator at least \(\sqrt{1+|X|^2}>2|X|\).
For \(s\ge89/100\), its numerator is at most
\(2(27/50)\sin(11\pi/100)<2(27/50)11\pi/100<1-27/50\).
The same argument holds with the two indices exchanged.
On the top triangle \(s+t\ge99/100\), the original factorial
endpoint bound gives
\[
 \Re F\le-\frac35\frac{99}{100}+\frac49+\frac{13}{300}
       <-\frac1{10}-\frac1{200}<\Re F_c-\frac1{250}.
 \tag{12}
\]
As in the earlier packet proofs, the finite endpoint loss is
polynomial in \(N\), and half-grid rounding preserves all strict
gaps, including the literal square cut \(i,j\le\lfloor N/40\rfloor\).

The original root-Pochhammer interpolant is regular on every
index rectangle: \(.46\le\Re(s+t)\le.9\) and
\((27/50)e^{2\pi(29/1000)}<1\). Its full symbol is unchanged.
Use the two exact cotangent formulas with these possibly asymmetric
rectangles. All twelve vertical-containing products are retained;
harmonic maximum principles extend their bounds to the connecting
side rectangles. Every nonconstant horizontal cotangent pays at
least \(2\pi(6/1000)\). Hence the horizontal excess in Section 2
leaves the strict alias gap
\[
                  2\pi\frac6{1000}-\frac1{50}>\frac1{100}.
 \tag{13}
\]
The constant cotangent products still combine to \(+N^2\).
They deform to the two critical index heights, strictly inside
their rectangles. Equation (11) gives the unique horizontal
maximum and a nonzero Gaussian determinant. The original cardinal
factors, symbol, and orientations are therefore exactly those of
the bidisk theorem, yielding (3), including its power and both
parities. The odd Gaussian term integrates to zero, leaving the
relative \(O(N^{-1})\) error.

All margins are strict and the domains are compact. They persist
on fixed open neighborhoods of the patches and of the output
union. The analytic branch is common on patch overlaps; Cauchy
estimates give fixed derivatives on smaller neighborhoods. This
proves Theorem 1 without continuing a value-only asymptotic.

## 4. Reproduction and scope

Run

```sh
python3 experiments/certify_three_vertex_real_input_union.py --precision 160
python3 experiments/replay_three_vertex_real_input_union.py --precision 192
```

The [author checker](../experiments/certify_three_vertex_real_input_union.py)
and [record](../repro/results/research-three-vertex-real-input-union.json)
contain every rational partition and fifteen scalar premises.
The [independent replayer](../experiments/replay_three_vertex_real_input_union.py)
and [record](../repro/results/research-three-vertex-real-input-union-replay.json)
reconstruct the complete cover and use the negative-frequency
dilogarithm primitive independently of the author's reflected
\(J\)-primitive. Neither checker imports an optimizer or accepts
sampled asymptotics.

This is an enlargement of an actual retained source domain. Restoring
the deleted corner uses the separate
[original Fourier-corner estimate](research_three_chain_fourier_corner_transfer.md).
Entrance estimates, propagation envelopes, and final bilinear
closing remain distinct source arguments.
