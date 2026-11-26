# Terminal conditional packets at ordinary endpoints

Research theorem, 5 November 2026. The final conditional factor in
the original one-cap open-word source has its complete nonzero packet
near every actual ordinary endpoint image. This supplies a local source
input; it does not estimate the rest of the open-word contour.

## 1. The complete source statement

Use the four endpoint graphs \(\mathcal K_{\epsilon,\delta}\), the
original phase \(Q_\epsilon\), and symbol \(A_\epsilon\) in the
[terminal source reduction](research_mixed_terminal_conditional_source_reduction.md).
Thus \(a\) lies in the complete external typed disk
\(D_{3+\delta}\), \(e=e(a)\) is the private endpoint leg of own
type \(3+\epsilon\), and the original conditional root is its
attached leg \(t=t(a)\). Every endpoint of every open word of
length \(m\ge2\) belongs to one of these four families.

**Theorem 1.** On a fixed ambient complex neighborhood of each compact
graph \(\mathcal K_{\epsilon,\delta}\), the original finite Laurent
polynomial satisfies
\[
\begin{split}
 C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie})
 &=N^{-(1+\epsilon)/2}\,
       B_\epsilon(a,e)\,
       e^{N[Q_\epsilon(t;a,e)-g(a)-g(e)]}
           (1+O(N^{-1})),\\
 B_\epsilon(a,e)
 &=\frac{\sqrt{2\pi}A_\epsilon(t;a,e)}
          {\sqrt{-Q_{\epsilon,ss}(t;a,e)}}\,
   \frac{e^{\pi i(a+e)/2}}
        {\sqrt{2\sin\pi a}\sqrt{2\sin\pi e}} .
\end{split}
\tag{1}
\]
Here \(t\) is the original root continued from its endpoint graph.
The square-root branches are the original nonzero factorial and
Gaussian branches. Both level parities, every finite row, and every
fixed asymptotic order are retained. The normalized error is
holomorphic and uniform with every fixed derivative on smaller
ambient neighborhoods.

In particular this is more than an estimate after substituting the
complete-color graph. A sufficiently small holomorphic perturbation
of the terminal variables remains in the same ambient neighborhood.
This includes the private-coordinate motion \(e(a,w_R)\) induced by
a nearby ordinary boundary color, wherever that critical continuation
is used. No new color-dependent finite conditional source is introduced;
the dependence is through its original two arguments.

## 2. Certified premises of the contour reduction

The accompanying [source record](../repro/results/research-mixed-terminal-conditional-source.json)
checks the original endpoint trees in full: 10,978 nodes, 5,258 accepted
root witnesses and 233 strict outside-disk exclusions. An accepted
parameter rectangle is omitted from the new source tests only if its
maximum squared normalized radius is strictly less than one. Therefore
every input disk boundary is covered by the retained original leaves.
Their counts in own/external type order are
\[
                   177,\quad180,\quad142,\quad133,
                 \qquad\text{total }632 .
\tag{2}
\]
The other 4,626 accepted witnesses are strictly interior and need no
new source test.

Each retained whole-cell root witness is revalidated against the
original three logarithmic equations. The same rational center and
inverse also validate a radius-\(10^{-10}\) midpoint disk. Parameter
derivatives use the original endpoint Jacobian, with five Neumann
terms and a rigorous geometric tail; they do not differentiate a
floating root. The new source tests prove
\[
\begin{split}
 M-\Re Q_\epsilon(.15),\ M-\Re Q_\epsilon(.49)&>1/1000,\\
 M-H_\epsilon(1)&>1/1000,\\
 M-\Re Q_\epsilon(x\pm .20i)+.40\pi&>1/10
                         \qquad(.15\le x\le.49).
\end{split}
\tag{3}
\]
All four holomorphic branches of \(H_\epsilon(1)\) are retained.
Each full horizontal side is covered by eight intervals. The exact
quartic/sextic right-tail polynomial is below one on its whole
required interval, covered by twelve intervals per original parameter
cell. No root proposal or parameter subdivision is added.

The older universal conditional contour lemma already supplies
curvature \( -\Re Q_{ss}>1/8\) and the increasing left real tail.
The source reduction transfers the actual real-tail and alias gaps
from the four circles throughout the disks, then to an ambient
neighborhood by zero-safe continuity and compactness. It does not
assert that the polynomial shape test itself extends inside.
Proposition 1 of that reduction now applies and gives the complete
packet for \(\mathcal L_{\epsilon,N}\). Dividing by the two original
marked factorial symbols gives precisely (1).

## 3. The one-cap identity remains unchanged

The exact source still contains
\[
 \mathcal U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^m C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal H_N(w_R,X_m^{-1})
 \prod_{j=1}^m\{d_N(X_j)(1+X_j^{-N})\}^{\epsilon_j},
\tag{4}
\]
with scalar \(\kappa^{m+\sum\epsilon_j}N^{m+\sum\epsilon_j}\)
and all original torus measures. The [complete first cap](research_mixed_complete_first_cap_packet.md)
and the exact identity
\(\mathcal H_N(w,e^{2\pi ie})=G_N(Ne)\mathcal C_N(e,w)\)
supply the separate endpoint factors on their stated domains.
Theorem 1 supplies the formerly missing final conditional kernel.

No Fourier branch is removed from (4), and no assertion is made
here about other conditional factors whose parameters leave their
proved domains, or about the remaining global open-word contour.
At length one the exact one-cap identity has no conditional factor,
so Theorem 1 is unnecessary there. No open-word noncancellation or
arbitrary short-filling theorem follows from this local statement.

The canonical and saved-replay commands are:

    python3 experiments/certify_mixed_terminal_conditional_source.py --precision 256
    python3 experiments/certify_mixed_terminal_conditional_source.py --precision 320 --input repro/results/research-mixed-terminal-conditional-source.json --output repro/results/research-mixed-terminal-conditional-source-replay.json
