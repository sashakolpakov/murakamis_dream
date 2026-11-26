# Index sides and aliases in the first complete-cap attachment

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This bounds the original finite index currents on the central wire
segment of the first attachment. It uses the exact retained summand,
including its cardinal factors. The actual cap bound and the real-index
complement are separate inputs; this note does not assert a complete
wire-cycle or arbitrary-chain asymptotic.

## 1. The source and the compact bounds

Use the literal corner-deleted source
\(\widetilde V_N(x,y)\) of
[the directed retained-packet theorem](research_three_vertex_directed_packet.md),
equation (2), and its exact sine-factorial/root-Pochhammer interpolant.
Let
\[
 y=x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 \frac7{50}\le\Re x\le\frac15,\qquad
 \frac{10135867}{10^8}\le\Im x\le\frac{10135871}{10^8}.
 \tag{1}
\]
The certified first-attachment height lies strictly in this interval,
including its \(10^{-8}\) root-enclosure error. Set
\[
 B=[1/4,9/20],\qquad h=1/50,\qquad
 \mathcal R=B+i[-h,h],\qquad
 \mathcal P(s,t;x,y)=F(s,t;x,y)-\pi i(x+y).
 \tag{2}
\]
Here \(F\) is the original phase in the
[joint Hessian theorem](research_three_vertex_joint_concavity.md), equation (1).
In particular \(\mathcal P\) includes both cardinal exponential
factors; it is not the index phase alone.

**Lemma 1.** Uniformly on (1), the following strict bounds hold:

* On each product of two sides of \(\partial\mathcal R\) with at
  least one vertical side,
  \[
                    \Re\mathcal P<323/500=.646.
  \tag{3}
  \]
* On each of the four products of horizontal sides,
  \[
                    \Re\mathcal P<7/10.
  \tag{4}
  \]

These include all four products of two vertical sides. Separate
maximum principles in the index variables extend (3) to a vertical
side times the whole other rectangle. They therefore also bound the
connecting currents when the other index contour moves within it.

*Proof.* Write \(X=e^{2\pi ix}\), \(Y=e^{2\pi iy}\),
\(U=e^{-2\pi is}\), \(V=e^{-2\pi it}\). On the present box,
\(|XU|,|YV|<1\) and \(1/2\le\Re(s+t)\le9/10\).
The original logarithmic branches are regular and agree with
\[
 \begin{split}
 \mathcal P={}&
 \frac{\operatorname{Li}_2(UV)-\pi^2/6
       -\operatorname{Li}_2(XU)+\operatorname{Li}_2(X)
       -\operatorname{Li}_2(YV)+\operatorname{Li}_2(Y)}{2\pi i}\\
 &+s\log X+t\log Y-\pi i(x+y).
 \end{split}
 \tag{5}
\]
This is the same continued primitive as the exact retained-source
interpolation, not a change of the additive phase constant.

The compact proof has sixteen domains, one for every ordered pair
of index sides. Their three real parameters are \(\Re x\) and the
two affine side coordinates. The narrow height interval in (1) is
retained in every interval derivative. The exact derivatives are
\[
 \begin{split}
 \mathcal P_s&=\log X+\log(1-UV)-\log(1-XU),\\
 \mathcal P_t&=\log Y+\log(1-UV)-\log(1-YV),\\
 \mathcal P_x&=2\pi is+\log(1-XU)-\log(1-X)-\pi i.
 \end{split}
 \tag{6}
\]
At each rational box center evaluate (5) by outward arithmetic;
bound its variation by the interval derivatives (6) times the exact
coordinate half-widths. The wire-height cost is
\((2\cdot10^{-8})\sup|\Im\mathcal P_x|\).
The saved certificate covers every domain by a disjoint complete
binary partition, with 269 accepted boxes in total. Every box proves
its designated strict threshold (3) or (4).

The independent replayer imports no author code. It checks exact
partition multiplicity one and encloses the full boxes using the
positive-exponential sine primitive at their centers,
\[
 \mathcal J(z)=-\frac{i\pi}{2}(z^2-z)
       +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iz})
       -\frac{i\pi}{12},
 \tag{7}
\]
together with the two separate denominator primitives in the original
formula for \(F\), and outward derivatives written using
\(\log(2\sin\pi(s+t))+i\pi(1/2-s-t)\).
Thus it independently retains the phase constant
and branch identity in (5). Its finite refinements of each accepted
box remain exact covers. No sampled maximum is used. The maximum
principles apply because the original phase is holomorphic on a fixed
neighborhood of \(\mathcal R^2\). \(\square\)

## 2. The actual cotangent currents

The exact interpolant before the two cardinal factors satisfies
\[
 \mathcal T_N(s,t)=N^{1/2}g(s,t;X,Y)e^{NF(s,t;X,Y)}
                         (1+O(N^{-1})),
 \tag{8}
\]
with the nonzero symbol and full physical-jet normalization of the
directed retained-packet theorem, equation (15). Multiplying by the
literal \(\kappa c_xc_y\) gives upper exponent \(\Re\mathcal P\).
The factors \((1-X^N)(1-Y^N)\) are uniformly bounded, and every
remaining factor costs only powers of \(N\).

Put the vertical sides at half-grid positions within \(O(N^{-1})\)
of \(1/4,9/20\). The strict compact margins above persist. The two
cotangent residue formulas recover exactly the original central finite
sum. On a vertical half-grid side the cotangent is bounded. Hence
every current containing a vertical side has upper rate (3), including
the two-vertical currents and the sides needed in subsequent deformations.

On a horizontal side at height \(\pm h\), the cotangent has its
constant value \(\mp i\) plus a remainder
\(O(e^{-2\pi Nh})\). Consequently every product with at least
one nonconstant factor has upper rate
\[
                       \frac7{10}-\frac{2\pi}{50}.
 \tag{9}
\]
The four constant products combine with the original positive factor
\(N^2\). They may move, using the already bounded side currents,
to the fixed horizontal plane through the actual two index heights.
Those heights lie strictly in \([-h,h]^2\). This is an identity for
the original finite interpolation at both parities, not a formal
replacement of the sum by an integral.

For clarity, suppose the independently estimated actual cap satisfies
\[
                  |W_N(x,0)|\le CN^A e^{253N/200}
 \tag{10}
\]
on the wire segment (1). Then the sides in the original integral
\(N\int W_N(x,0)\widetilde V_N(x,x_h)\,dx\) have rate below
\[
 \frac{253}{200}+\frac{323}{500}=1.911
          <\Re\Theta_*-\frac1{5000},
 \qquad \Re\Theta_*>1.9113.
 \tag{11}
\]
The alias products have a still larger gap, since
\[
 \frac{253}{200}+\frac7{10}-\frac{2\pi}{50}<1.84.
 \tag{12}
\]
Here the source measure \(N\), both residue factors, and the finite
symbols only change polynomial prefactors. The nonzero central
coefficient is supplied by the actual local cap and retained packets
and their joint saddle, not by these upper bounds.

All bounds retain the original finite source and its parity phases.
Strict margins give a small complex neighborhood in the fixed outgoing
wire. If (10) is available uniformly with ordinary outside-color
normals, the identical current estimates retain those normals because
the outside variable occurs only in the actual cap factor. This does
not establish (10), the real-index complement, the cap angular currents,
or an arbitrary-chain estimate.

## 3. Reproduction

Run

```sh
python3 experiments/certify_three_attachment_index_currents.py --precision 160
python3 experiments/replay_three_attachment_index_currents.py --precision 192
```

The [author checker](../experiments/certify_three_attachment_index_currents.py)
and [cover](../repro/results/research-three-attachment-index-currents.json)
retain all sixteen domains and rational leaves. The
[independent replayer](../experiments/replay_three_attachment_index_currents.py)
and [record](../repro/results/research-three-attachment-index-currents-replay.json)
retain the exact-cover audit and outward primitive verification.
