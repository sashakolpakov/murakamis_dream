# Complete conditional sources on the reduced universal leg disks

Research theorem, 5 November 2026. The complete six-domain certificate
verifies the source inequalities on 4,409 affine root cells in both
conditional orientations. The domains use the smaller output disks
of the original local maps; they
are not the larger disks on which an absolute revived-row gap is known
to fail.

## 1. The six universal families

Put
\[
 P_3=\{|z-(.35-.01i)|\le.083\},\qquad
 P_4=\{|z-(.30-.052i)|\le.060\}.
 \tag{1}
\]
Both closed disks lie strictly inside the corresponding original
\(D_3,D_4\) in
[universal block localization](research_mixed_cyclic_critical_localization.md).
For each own type \(3+\epsilon\) and external types \(3+\alpha,3+\beta\),
the original zero-lift two-leg block map is therefore holomorphic on
a neighborhood of \(P_{3+\alpha}\times P_{3+\beta}\):
\[
\begin{split}
 0&=g'(s+t)+g'(s+a)-(2+\epsilon)g'(s)+2\pi ia,\\
 0&=g'(s+t)+g'(t+b)-(2+\epsilon)g'(t)+2\pi ib .
\end{split}
\tag{2}
\]
The root \((s,t)\) stays in the original own typed disk and in
\(\mathcal Q=\{.23<\Re z<.45,\ |\Im z|<.12\}\).
Swapping \(a,b\) swaps \(s,t\). It suffices to use the six
own/unordered-external-type cases and to retain both conditional
orientations in every case.

Keep the whole fixed-\(N\) canonical source
\[
\begin{split}
 \mathcal L_{\epsilon,N}(A,B)
 &=\widehat P_N(NA)\widehat P_N(NB)
   \sum_{j=0}^{N-1}
    \frac{e^{2\pi iAj}(r^{NA+1};r)_j(r^{NB+1};r)_j}
         {(r;r)_j^{2+\epsilon}},\\
 Q_\epsilon(z;A,B)
 &=g(z+A)+g(z+B)-(2+\epsilon)g(z)+2\pi iAz .
\end{split}
\tag{3}
\]
Its two required orientations are
\((z,A,B)=(s,a,t)\) and \((t,b,s)\).
All finite rows, including those revived off the physical lattice,
remain in (3).

**Theorem 1.** Uniformly on every product (1), both orientations satisfy
\[
 \mathcal L_{\epsilon,N}(A,B)
 =N^{(1-\epsilon)/2}
   \frac{\sqrt{2\pi}A_\epsilon(z;A,B)}
        {\sqrt{-Q_{\epsilon,zz}(z;A,B)}}
   e^{NQ_\epsilon(z;A,B)}(1+O(N^{-1})),
\tag{4}
\]
with the original nonzero factorial symbol
\[
 A_\epsilon(z;A,B)=
 e^{\pi i(\epsilon z-A-B)/2}
 \frac{\sqrt{2\sin\pi(z+A)}\sqrt{2\sin\pi(z+B)}}
      {(2\sin\pi z)^{1+\epsilon/2}} .
\tag{5}
\]
The original Gaussian and sine branches, both level parities and every
fixed asymptotic order are retained. The corresponding literal \(C\)
packet has phase \(Q_\epsilon(z)-g(A)-g(B)\), power
\(N^{-(1+\epsilon)/2}\), and symbol (5) divided by the two marked
factorial symbols. It holds on an ambient neighborhood of the compact
conditional image, with fixed holomorphic derivatives there.

## 2. Old analytic inputs and the new finite source tests

All four legs in (2) are in \(\mathcal Q\). Consequently
[the original contour reductions](research_mixed_conditional_image_contours.md)
give, without any new curvature cover,
\[
 -\Re Q_{\epsilon,zz}>1/8
 \quad\text{on }[\ell,u]+i[-h,h],\qquad
 \ell=.15,\quad u=.49,\quad h=.20.
\tag{6}
\]
The complete real-row rate is
\[
\begin{split}
 H_\epsilon(v;A,B)
 ={}&\Re g(A)+\Re g(B)
 +\int_0^v\log|1-e^{-2\pi i(A+x)}|\,dx\\
 &+\int_0^v\log|1-e^{-2\pi i(B+x)}|\,dx
 -(2+\epsilon)J(v)-2\pi v\Im A .
\end{split}
\tag{7}
\]
It increases on \((0,\ell]\) by the already proved bound
\(H_\epsilon'\ge\log4-.24\pi>1/2\). At either real cut,
\(H_\epsilon(c)=\Re Q_\epsilon(c)\).

On the distinguished boundary of each product (1), the new certificate
checks in both orientations, with \(M=\Re Q_\epsilon(z;A,B)\),
\[
\begin{split}
 M-\Re Q_\epsilon(\ell),\ M-\Re Q_\epsilon(u)&>1/1000,\\
 M-\Re g(A)-\Re g(B)-2\pi(-\Im A)_+-2\pi(\Im B)_+&>1/1000,\\
 M-\Re Q_\epsilon(x\pm ih)+2\pi h&>1/10
                                   \quad(\ell\le x\le u).
\end{split}
\tag{8}
\]
The second line keeps all four holomorphic last-row branches.
The exact right-tail polynomial is also bounded strictly below one:
\[
\begin{split}
 &4^{-\epsilon}e^{2\pi(\Im B-\Im A)}
 |\cos\pi A-w\sin\pi A|^2|\cos\pi B-w\sin\pi B|^2
                                       (1+w^2)^\epsilon<1,\\
 &-\cot(\pi u)\le w\le
       \max\{\Re\cot(\pi A),\Re\cot(\pi B)\}.
\end{split}
\tag{9}
\]
The contour lemma therefore reduces the entire right real tail to
its endpoints \(u,1\). In particular its revived endpoint is not
discarded.

## 3. Root witnesses, response and exact coverage

Parametrize the two boundary circles by independent real angles
\((\theta,\varphi)\in[0,1]^2\). A proposal supplies rational centers
\(z_0=(s_0,t_0)\), a rational inverse matrix \(Y\), a rational affine
response matrix \(D\), and two positive rational remainder radii.
The certified center over a parameter rectangle is
\(z_0+D(p-p_0)\), where \(p=(a,b)\).
The original logarithmic Taylor remainder and the interval Jacobian
verify a self-map of the two remainder disks, exactly as in the old
universal block primitive. Only these outward inequalities accept a
cell. The original equations fix the zero lift; all roots remain in
the original own disk and \(\mathcal Q\).

The same saved center and inverse validate a small midpoint root
disk. The parameter response of the actual root is
\[
 -J^{-1}
 \operatorname{diag}\left(
 \frac{2\pi i}{1-e^{-2\pi i(s+a)}},
 \frac{2\pi i}{1-e^{-2\pi i(t+b)}}\right).
\tag{10}
\]
It is enclosed with the interval Jacobian and a verified Neumann tail.
For a cut or horizontal contour point \(c\), the source-gap
derivatives use stationarity:
\[
 G_A=g'(z+A)-g'(c+A)+2\pi i(z-c),\qquad
 G_B=g'(z+B)-g'(c+B).
\tag{11}
\]
The two external derivatives are \(G_A\) in the corresponding
external coordinate plus \(G_B\) times the response of the other
inner leg. The four last-row branches use the same rule, with
the exact derivatives of \(g(A),g(B)\) and both linear penalties
retained. Circle derivatives and real-part mean-value bounds
enclose every point of the parameter cell.

All horizontal segments and all intervals in (9) are covered
as complete intervals, not sampled. Each of the six angle squares
has an exact complete binary tree. Saved mode validates the same
trees and every rational witness, without new proposals or
refinement. Runtime and node budgets bound the author run.

## 4. Complete contour and ambient source scope

The inequalities above control all original real rows on the
distinguished boundaries. For each fixed real row, its rate minus
the selected harmonic action is separately subharmonic in the
original external variables \(a,b\). Two maximum principles
transfer the actual tail gap to the full product. The cut and
horizontal gaps are harmonic and extend in the same way. No
interior extension of the polynomial shape test (9) is presumed.

The roots lie in \(\mathcal Q\), at real distance greater than .04
from both cuts. Curvature (6) therefore supplies a positive endpoint
gap on the horizontal line through each saddle. Height convexity
controls both zero-mode joins and every half-grid vertical alias.
The unchanged cotangent coefficient is \(+N\); the summand has
power \(N^{-\epsilon/2}\), and one Gaussian gives (4). Uniform
zero-safe product estimates retain both physical endpoints and
all revived rows. Every strict margin persists under half-grid
rounding and on slightly enlarged compact parameter domains.

The conditional target image has an actual ambient neighborhood.
For example the derivative of \((a,b)\mapsto(a,t(a,b))\) has
nonzero determinant:
\[
 t_b=-\frac{J_{11}}{\det J}\,
            \frac{2\pi i}{1-e^{-2\pi i(t+b)}}\ne0 .
\tag{12}
\]
Here \(J_{11}\) is the first diagonal entry, whose real part is
negative by (6), and the full block Jacobian is nonsingular by
the old theorem. Local inverse maps and uniqueness of the
conditional root glue the same finite-source packet throughout
this neighborhood. The opposite orientation is identical.

This is a theorem for one complete conditional factor. When an
open-word geometry theorem places its two external legs in (1),
it supplies that factor's source germ without enumerating word
lengths. It does not estimate the full remaining torus, discard
any \(d_N(1+X^{-N})\) weight, or prove open-word noncancellation.

The finite grid diagnostic in
[the archive](../repro/diagnostics/2026-11-05-reduced-disk-conditional-sources/README.md)
only motivated these domains. Its sampled margins are not used
in the outward certificate.

## 5. Certificate and reproduction

The complete outward cover has six type products, 4,409 accepted
affine root cells and 8,812 tree nodes. The case counts in the order
\((\epsilon,\alpha,\beta)=(0,0,0),(0,0,1),(0,1,1),
(1,0,0),(1,0,1),(1,1,1)\) are respectively
1,157, 1,033, 960, 529, 406 and 324. Every cell retains both
orientations, the original logarithmic root lift, all eight horizontal
intervals on each side and all twelve right-tail intervals.
The canonical record binds this proof, the certifier and fourteen
current input files. Full rational affine root enclosures are saved;
no additional geometric inequality is an acceptance condition.

Author reproduction:

```sh
python3 experiments/certify_mixed_reduced_disk_conditional_packets.py --precision 256 --output repro/results/research-mixed-reduced-disk-conditional-packets.json
```

Independent saved-cell replay, with no proposals or refinement:

```sh
python3 experiments/certify_mixed_reduced_disk_conditional_packets.py --precision 320 --input repro/results/research-mixed-reduced-disk-conditional-packets.json --output repro/results/research-mixed-reduced-disk-conditional-packets-replay.json
```
