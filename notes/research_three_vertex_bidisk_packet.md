# A genuine bidisk for the original retained three-crossing packet

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This gives an explicit source domain containing both signs of every
wire displacement from the homogeneous point. It uses a slightly larger
exact deleted corner than the earlier directed-tube theorem. The
original-source error of that change is independently controlled; no
cycle coefficient is inferred from the analytic extension of a phase.

## 1. The finite source and theorem

Set
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 \mathcal Q=\{x_h+u+iv:|u|,|v|\le1/200\},\qquad
 L_{40}=\lfloor N/40\rfloor.
 \tag{1}
\]
Retain the original crossing and cardinal conventions, and define
\[
 \begin{split}
 E_{40}&=M^TP_{L_{40}}JM P_{L_{40}}M,\\
 \widetilde A^{(40)}&=JM^3-E_{40},\\
 \widetilde V_N^{(40)}(x,y)&=h(x)^T\widetilde A^{(40)}h(y).
 \end{split}
 \tag{2}
\]
The exact finite double sum is the one in the
[traced-vertex identity](research_traced_three_vertex_endpoint.md),
equation (6), with precisely the square \(i,j\le L_{40}\) removed.
For all sufficiently large levels this square lies inside \(i+j<N\).
No other rows, values or physical first normals are modified.

**Theorem 1.** On a fixed open complex neighborhood of
\(\mathcal Q\times\mathcal Q\),
\[
 \widetilde V_N^{(40)}(x,y)=
       \kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}(1+O(N^{-1})).
 \tag{3}
\]
The phase and amplitude are the original homogeneous branches;
\(a\) is holomorphic and nowhere zero. The normalized error is
holomorphic and uniformly \(O(N^{-1})\), including each fixed
parameter derivative on a smaller neighborhood. Both level parities
are retained. In particular (3) holds on the genuine closed bidisk
\(|x-x_h|,|y-x_h|\le1/200\).

The superscript \((40)\) matters: earlier directed source packets
use the different cutoff \(\lfloor N/50\rfloor\). Their local
phases and amplitudes agree on overlaps, but their finite sources
are not silently identified.

## 2. Critical branch and compact comparisons

Use the exact original phase \(F(s,t;X,Y)\) and its interpolant
from the [directed-packet proof](research_three_vertex_directed_packet.md),
equations (4), (15). Put \(X=e^{2\pi ix}\), \(Y=e^{2\pi iy}\),
and
\[
 \begin{gathered}
 \alpha=X^{-1}-1,\quad\beta=Y^{-1}-1,\quad
 \Delta=1-2(\alpha+\beta)+(\alpha-\beta)^2,\\
 U_c=(1+\alpha-\beta-\sqrt\Delta)/2,\quad
 V_c=(1-\alpha+\beta-\sqrt\Delta)/2,\\
 s_c=i\Log U_c/(2\pi),\quad t_c=i\Log V_c/(2\pi),\quad
 F_c=F(s_c,t_c;X,Y).
 \tag{4}
\]
The compact certificate proves throughout \(\mathcal Q^2\):
\[
 \begin{gathered}
 \Im\Delta>0,\quad U_c,V_c\text{ in the lower-left quadrant},\\
 \Re X,\Im X,\Re Y,\Im Y>2/25,\quad |X|,|Y|<27/50,\\
 3/10<\Re s_c,\Re t_c<2/5,\quad
 |\Im s_c|,|\Im t_c|<3/200,\quad \Re F_c>-1/10.
 \end{gathered}
 \tag{5}
\]
The index equations have their original lifts: their exponentials
are one by (4), they are holomorphic on this connected parameter
domain, and their values at homogeneity are zero.

Let
\[
 B=[1/4,9/20],\qquad h=17/1000,\qquad
 \mathcal R=B+i[-h,h],\qquad \epsilon=1/40.
 \tag{6}
\]
The remaining certified inequalities are:

* On each of the three real-index sets
  \[
  \begin{split}
  E_0&=\{0\le s\le\epsilon,\ \epsilon\le t,\ s+t\le99/100\},\\
  E_1&=\{\epsilon\le s\le1/4,\ 0\le t,\ s+t\le99/100\},\\
  E_2&=\{s=9/20,\ 0\le t\le54/100\},
  \end{split}
  \qquad \Re(F_c-F)>1/200.
  \tag{7}
  \]
* On every product of two sides of \(\partial\mathcal R\) with
  at least one vertical side,
  \[
                         \Re(F_c-F)>1/10000.
  \tag{8}
  \]
* On the four products of horizontal sides,
  \[
                         \Re(F-F_c)<1/20.
  \tag{9}
  \]

Here every assertion is uniform in both complex wire parameters.
It is essential to choose the index contour in (6): the taller
\(\pm.02\) contour used in earlier proofs does not satisfy the
same positive side margins on this symmetric parameter square.

For completeness, the certificate uses one four-dimensional domain
for the branch bounds in (5). Separately harmonic functions
\(\Re F_c\) and \(\Re(F_c-F)\) attain their boundary extrema on
the products of the four sides of each wire square. All sixteen
ordered pairs of wire sides are retained. There are sixteen floor
domains, forty-eight domains (7), and 256 index-side products (8)--(9).
This is an exhaustive 321-domain cover. Each accepted rational box
uses an outward center value and full interval derivative bound;
the record contains all 17,292 accepted boxes.

## 3. Entire finite complement, aliases, and the coefficient

The proof now uses the original residue identity, not a continuation
of a pointwise asymptotic. On real indices,
\[
 \partial_s\Re F=
       \log\frac{2|X|\sin\pi(s+t)}{|1-Xe^{-2\pi is}|}.
 \tag{10}
\]
For \(9/20\le s\le9/10\),
\(1/4<s-\Re x<3/4\), so the denominator is at least
\(\sqrt{1+|X|^2}>2|X|\). For \(s\ge9/10\), the numerator
is at most \(2(27/50)\pi/10<1-27/50\). Thus all high-index
parts below the top collar reduce to \(E_2\); interchange indices
and wire parameters for the other high strip. The sets (7), together
with this reduction and the exact deleted corner, cover the full
retained real-index complement of \(B^2\).

On \(s+t\ge99/100\), the elementary bounds
\(\log|X|,\log|Y|<-3/5\),
\(\operatorname{Li}_2(27/50)<2/3\), and
\(\mathcal J(s+t)<13/300\) give
\[
 \Re F\le-\frac35\frac{99}{100}+\frac49+\frac{13}{300}
          <-\frac1{10}-\frac1{200}<\Re F_c-\frac1{200}.
 \tag{11}
\]
The exact endpoint factorial bounds cost only powers of \(N\),
including \(s+t\) within \(O(N^{-1})\) of one. The rounding of
\(L_{40}\) and the half-grid cuts at the ends of \(B\) preserve
all strict compact gaps. No interpolation of the top factorial
endpoint is required.

On \(\mathcal R^2\), the exact root-Pochhammer interpolant is
regular: \(|X|e^{2\pi h},|Y|e^{2\pi h}<1\) and
\(1/2\le\Re(s+t)\le9/10\). Its full original symbol is
\[
 \mathcal T_N=N^{1/2}g e^{NF}(1+O(N^{-1})),\qquad
 g=\frac{\sqrt{2\sin\pi(s+t)}e^{-i\pi(s+t)/2}}
 {\sqrt{(1-X)(1-Xe^{-2\pi is})(1-Y)(1-Ye^{-2\pi it})}}.
 \tag{12}
\]
The two cotangent formulas with half-grid vertical sides recover the
literal central sum. Equation (8) bounds every side current, including
both-vertical products. Maximum principles in the other index give
the same bound on the connecting side rectangles. On the horizontal
sides, every nonconstant cotangent factor pays \(e^{-2\pi Nh}\).
By (9), its net loss is strictly greater than
\[
                         2\pi h-1/20>1/20.
 \tag{13}
\]
The four constant products combine with coefficient \(+N^2\),
and move to the horizontal plane through \((s_c,t_c)\). Their
heights lie strictly inside (6).

The wire squares in (1) lie inside the joint-concavity box, and
\(\mathcal R^2\) lies inside its index box. The
[proved positive Hessian](research_three_vertex_joint_concavity.md)
therefore makes \((s_c,t_c)\) the unique maximum on that horizontal
plane. Gaussian integration, with the original orientations, gives
\[
 \Phi=F_c-\pi i(x+y),\qquad
 a=\frac{2\pi\sqrt{XY}\,g(s_c,t_c;X,Y)}
                          {\sqrt{\det(-F''(s_c,t_c))}}.
 \tag{14}
\]
Accretivity makes the determinant nonzero. The square root continues
from the homogeneous normalization on the simply connected wire
domain. The two literal cardinal factors contribute \(N^{-2}\),
\(\sqrt{XY}\), their affine exponential, and exponentially small
factors \((1-X^N)(1-Y^N)\). Thus the power is \(N^{-1/2}\)
and the coefficient is precisely (14). The first odd Gaussian term
integrates to zero, leaving relative \(O(N^{-1})\).

All estimates are strict on compact sets. They persist on an open
neighborhood of \(\mathcal Q^2\), and Cauchy estimates give the
asserted fixed parameter derivatives. This proves Theorem 1 without
a parity restriction. The exact finite interpolant already preserves
the original physical jets; no value-only reconstruction enters.

## 4. Original-source comparison and reproduction

The [Fourier corner-transfer theorem](research_three_chain_fourier_corner_transfer.md),
Section 4, proves that the new corner has operator rate
\[
 \sigma_{40}=(\log80+1)/40<27/200.
 \tag{15}
\]
For any fixed complete-ended original all-three chain its effect
has rate at least \(31/600\) below the geometric action. Its mixed
ordinary/Fourier two-vertex error has rate below \(1.715\), with
the original outside normals retained. These are separate full-source
estimates; they justify choosing the larger corner in a later
composition. They do not by themselves control the wire complement
of an iterated composition, nor give the initial cap packet on an
explicit output disk.

Run

```sh
python3 experiments/certify_three_vertex_bidisk_packet.py --precision 160
python3 experiments/replay_three_vertex_bidisk_packet.py --precision 192
```

The [author checker](../experiments/certify_three_vertex_bidisk_packet.py)
and [record](../repro/results/research-three-vertex-bidisk-packet.json)
contain all rational covers. The
[independent replayer](../experiments/replay_three_vertex_bidisk_packet.py)
imports no author code, reconstructs every exact binary partition,
and uses the negative-frequency dilogarithm primitive independently
of the author's sine primitive. Its
[record](../repro/results/research-three-vertex-bidisk-packet-replay.json)
records the full higher-precision replay and thirteen endpoint/alias
comparisons. The earlier unsuccessful taller-contour attempts saved
no certificate and are not used as evidence.
