# A selected minimum-level flow need not increase the phase

Research proof, 4 November 2026. This is an obstruction to a proposed
monotonicity argument, not to a net selected-term gap, a finite-source
asymptotic or an outer-integral estimate.

Use the original seven-cycle with all vertices of type four, and select
all seven outer Fourier factors. The selected coefficient is
\(H=7/500\). On the exact minimum-neighbor contour put
\[
 h_j=H\min\{\rho(x_{j-1}),\rho(x_j),\rho(x_{j+1})\},\qquad
 \rho(x)=\frac{x-.10}{.12}\quad(.10\le x\le.22),
 \qquad\rho=1\text{ on }[.22,.45].                         \tag{1}
\]
Indices are taken modulo seven. The complete periodic cutoff and exact
Laurent contour identity are unchanged from the
[minimum-neighbor theorem](research_mixed_minimum_neighbor_contour.md).

Choose the exact rational real coordinates
\[
 x=\left(\frac9{20},\frac{197}{1000},\frac{49}{250},
          \frac{197}{1000},\frac{23}{100},\frac7{20},\frac7{20}\right).
                                                               \tag{2}
\]
The corresponding heights are
\[
 h=\left(\frac{679}{60000},\frac7{625},\frac7{625},
               \frac7{625},\frac{679}{60000},\frac7{500},\frac7{500}\right).
                                                               \tag{3}
\]
Coordinate two is the unique real minimum. Increase only that coordinate
by \(\tau\), with \(-1/1000<\tau<1/1000\). The exact graph changes
only heights one, two and three, each at derivative
\[
                           H\rho'=\frac7{60}.                \tag{4}
\]
The outer heights zero and four remain fixed: their controlling
neighbors have real coordinate \(197/1000\). Thus (4) uses the actual
neighbor correlations, not independently released height boxes.

## 1. The actual two Fourier branches

Let \(\phi=\phi_{11}\) be the original allocated conditional action:
\[
 \phi(a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias
                           -\frac32[g(a)+g(b)],              \tag{5}
\]
where \(s=s_*(a,b)\) is the unique original zero-lift root.
All coordinates and nearby flow points lie in the proved
[transition/plateau source polygons](research_mixed_transition_pair_source.md).
In particular (5) is the calibrated phase of the complete canonical
source; root uniqueness is not substituted for a source statement.

The full selected Fourier upper-rate profile is
\[
 \mathcal H(z)=\Re\sum_{j=0}^6\phi(z_j,z_{j+1})
                 +\sum_{j=0}^6\max\{\Re g(z_j),-2\pi\Im z_j\}.
                                                               \tag{6}
\]
This retains both the forcing and factorial alternatives of the literal
Fourier polynomial and the selected monomial. At the three moving
coordinates the maximum strictly selects the second alternative.
The checker proves
\[
                 -\Re g(z_j)-2\pi\Im z_j>\frac1{20},
                            \qquad j=1,2,3.                 \tag{7}
\]
All other coordinates are fixed along this flow, so their chosen
alternatives add constants and do not affect its derivative.

More generally, throughout
\(1/10\le x\le11/50\), \(0\le h\le7/500\),
\[
                 -\Re g(x+ih)-2\pi h>\frac3{40}.             \tag{8}
\]
For completeness, the expression is strictly concave in \(x\), because
its second derivative is \(-\pi\Re\cot\pi(x+ih)<0\). It strictly
decreases in \(h\), since
\(\partial_h[-\Re g]-2\pi=\Arg(1-e^{2\pi h-2\pi ix})-2\pi<0\).
Its minimum is therefore at one of the two real endpoints with
\(h=7/500\). Two outward dilogarithm comparisons prove (8).
This useful branch reduction does not itself prove a phase gap.

## 2. An outward negative derivative

Write \(z_j=x_j+ih_j\), and define
\[
 G_j=\phi_b(z_{j-1},z_j)+\phi_a(z_j,z_{j+1})+2\pi i,
                         \qquad j=1,2,3.                    \tag{9}
\]
The exact original derivatives are
\[
 \phi_a=g'(s+a)+2\pi is-\frac32g'(a),\qquad
 \phi_b=g'(s+b)-\frac32g'(b).                                \tag{10}
\]
By (4), (6) and the strict branch margins (7),
\[
 \left.\frac{d}{d\tau}\mathcal H(z(\tau))\right|_{\tau=0}
       =\Re G_2-\frac7{60}\Im(G_1+G_2+G_3)<-\frac45.         \tag{11}
\]
Four independent original-logarithm Newton self-maps enclose the roots
for the four incident edges. Each enclosure stays in the selected
cotangent strip, fixing the original logarithmic lift. Direct outward
evaluation of (10) then gives the informational interval
\(-.8628775675\pm1.7\cdot10^{-11}\); the exact acceptance threshold
is (11). No floating root or sampled derivative is accepted as evidence.

All inequalities are strict and the controlling graph incidences are
unchanged for sufficiently small positive or negative \(\tau\). Hence the
true profile (6) decreases on a nonempty interval immediately below
\(.196\), as its unique real minimum is raised to that value. In particular,
a branchwise nondecreasing selected minimum-level transport up to the
four-fifths height threshold is false on this original contour.

The initial profile may already lie below its geometric target; nothing
here contradicts that possibility. An integrated allowance, a different
transport path or a different periodic contour might still prove the
needed global selected upper bound. The unselected minimum-level
certificate has different height coefficients and is unaffected.

## 3. Reproduction

```sh
python3 experiments/check_mixed_selected_minimum_flow_obstruction.py --precision 256
```

The checker uses exact rational coordinates, graph incidences and flow
rates, then outward critical-root and phase calculations. It binds the
actual contour, global root and complete polygon-source inputs.
