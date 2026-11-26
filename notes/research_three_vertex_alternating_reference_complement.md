# Real-index tails of the undeleted three-crossing vertex at the alternating reference

Research lemma, 4 November 2026. All earlier source artifacts and frozen
manuscripts are unchanged.

The full transformed triangle, including its endpoint corner, has a
strictly small real-index complement at the validated alternating
power-three/power-four reference. This supplies one part of a local
undeleted vertex contour; it asserts no mixed-word global coefficient.

## 1. Reference and original summands

Let \(a\) be the already validated root of
\[
 4a^4-6a^3+4a^2-2a+1=0,
 \quad a\simeq.772606299919327+.357976514994012i.
 \tag{1}
\]
Define, with the original selected branches,
\[
 B=\frac{a^2(2a-1)^2}{2(a-1)},\qquad
 x_0=\frac1\pi\arcsin\sqrt{\frac{a^2B}{a^2+B}},\qquad
 K=e^{2\pi ix_0}=A+iD,
 \quad r=|K|,\quad \xi=\Re x_0.
 \tag{2}
\]
The [reference proof](research_three_four_source_interface.md) fixes these
branches and the original unexponentiated periods. The new checker
rechecks a Newton self-map on the same exact rational center and radius,
and verifies all inherited provenance. Its resulting bounds include
\[
 \begin{split}
 K&\simeq.249206722431137+.556578915645297i,\qquad
 \xi\simeq.182999107379803,\quad r\simeq.609822990584780,\\
 0&<\xi<1/4,\quad D>0,\quad r^2>A,\quad
 1-3r^2+2A>0,\quad
 |1-Ke^{-9\pi i/10}|^2-4r^2>0.
 \end{split}
 \tag{3}
\]
Only the outward comparisons, not the displayed decimal approximations,
are used below.

Use the literal undeleted finite formula from
[the traced-vertex proof](research_traced_three_vertex_endpoint.md#2-an-exact-two-variable-formula).
At \(x=y=x_0\), its summand with indices \(i,j\ge0\), \(i+j<N\),
has absolute upper exponent
\[
 E(s,t)=-\log r+\mathcal J(s+t)+(s+t)\log r-I_K(s)-I_K(t),
 \quad s=i/N,\quad t=j/N,
 \tag{4}
\]
where
\[
 \mathcal J(p)=\int_0^p\log(2\sin\pi u)\,du,\qquad
 I_K(s)=\int_0^s\log|1-Ke^{-2\pi iu}|\,du.
 \tag{5}
\]
In particular \(E(0,0)=-\log r\) is retained. The two cardinal
factors in the exact source produce \(-\log r\). The denominator
products have uniform Riemann-sum error \(O(1)\) because \(r<1\),
and the numerator sine factorial has its original uniform
\(O(\log N)\) error through both ends. Thus (4) bounds the literal
finite summands with only polynomial prefactors, at both parities.

## 2. An exact reduction of the full triangle

Put \(b=9/20\). For \(s,t>0\), \(p=s+t<1\),
\[
 E_s=\log\frac{2r\sin(\pi p)}{|1-Ke^{-2\pi is}|}.
 \tag{6}
\]
**Lemma 1.** Throughout the triangle, \(E_s<0\) whenever \(s\ge b\),
and likewise for \(E_t\) when \(t\ge b\).

*Proof.* For \(b\le s\le1/2\), the denominator in (6) increases
with \(s\), since \(0<s-\xi<1/2\). The final inequality of (3)
therefore puts it strictly above \(2r\), proving the claim.
For \(s\ge1/2\), \(\sin(\pi p)\le\sin(\pi s)\). Direct expansion gives
\[
 \begin{split}
 |1-Ke^{-2\pi is}|^2-4r^2\sin^2(\pi s)
   &=1-r^2+2(r^2-A)\cos(2\pi s)-2D\sin(2\pi s)\\
   &\ge1-3r^2+2A>0,
 \end{split}
 \tag{7}
\]
since \(D>0\), \(r^2>A\), and \(\sin(2\pi s)\le0\).
Continuity includes the triangle endpoints. Symmetry gives the other
coordinate. No fixed-sum substitution or omitted boundary is used.
\(\square\)

**Lemma 2.** On the entire closed triangle \(s,t\ge0\), \(s+t\le1\),
outside \([1/4,9/20]^2\),
\[
                              E(s,t)<13/20=.650.
 \tag{8}
\]

*Proof.* If an index exceeds \(9/20\), decrease it to that value;
Lemma 1 only increases the envelope. If necessary do the same to the
other index. Such a point is bounded by one of the two faces
\(s=9/20,0\le t\le9/20\), or its transpose. If both indices already
lie below \(9/20\), being outside the central square means that one
lies below \(1/4\). It is then in
\([0,1/4]\times[0,9/20]\), or its transpose. Consequently only
\[
 [0,1/4]\times[0,9/20],\qquad
 \{9/20\}\times[0,9/20]
 \tag{9}
\]
need to be checked, using exact symmetry of (4). These sets retain
all axes and the original corner.

The outward certificate covers the first rectangle by 48 dyadic
leaves and the second interval by 9. On every leaf it evaluates (4)
and, where useful, its rigorous centered mean-value upper bound from
(6). Near \(p=0\) it uses the continuous sine-primitive bound, never
a logarithmic derivative at zero. The independent replay uses the
opposite-frequency dilogarithm formula, rebuilds the exact binary
partition and checks all scalar premises in (3). Each leaf has upper
bound strictly below \(13/20\). This proves (8). \(\square\)

## 3. Actual-source consequence and scope

The original undeleted real-index complement therefore obeys
\[
 \left|\sum_{(i/N,j/N)\notin[1/4,9/20]^2}
                 \text{original summand}_{ij}(x_0,x_0)\right|
 \le CN^q e^{.650N}.
 \tag{10}
\]
The estimate holds for the sum of absolute summands and for every
subset. Every fixed derivative in either Fourier boundary costs only
a polynomial, because both denominator circles remain strictly inside
the unit disk. No value-only representative or corner deletion has
been substituted for the original traced vertex.

The envelope for independently varying complex \(x,y\) is
\(-\tfrac12\log|XY|+\mathcal J(s+t)+s\log|X|+t\log|Y|-I_X(s)-I_Y(t)\).
It is continuous uniformly on the compact closed index triangle when
\(|X|,|Y|<1\). Hence (10) holds with the slightly weaker rate \(.651\)
on some fixed complex neighborhood of \((x_0,x_0)\), including all
fixed derivatives after shrinking that neighborhood. This is an
existence assertion for a neighborhood, not a quantified radius.
The central principal contour, its index sides and aliases, its
nonzero coefficient and any mixed-word composition are separate inputs.

## 4. Reproduction

```sh
python3 experiments/certify_three_vertex_alternating_complement.py --precision 192
python3 experiments/replay_three_vertex_alternating_complement.py --precision 256
```

The source reference is the current passed
[interface record](../repro/results/research-three-four-source-interface.json).
The new author and replay records retain the two exact covers, the
fresh scalar root check and all current dependency hashes.

The [author](../experiments/certify_three_vertex_alternating_complement.py)
and [record](../repro/results/research-three-vertex-alternating-complement.json),
and the [independent replay](../experiments/replay_three_vertex_alternating_complement.py)
and [record](../repro/results/research-three-vertex-alternating-complement-replay.json),
check all 57 leaves and nine strict scalar comparisons.
