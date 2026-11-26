# Zero-uniform low/plateau clusters on an exact coupled contour

Research proof, 4 November 2026. This combines completed whole-source
bounds with the full matrix reset estimate. It concerns the unaliased
term on one specified coupled contour. Other regions and selected
outer aliases remain separate.

## 1. The exact contour and its restricted region

Fix any cyclic three/four word of length \(m\ge1\). Let \(z_j^*\)
be its original critical outer coordinates, with heights \(h_j^*\),
and let \(M\) be its original critical real action. In particular
\(|h_j^*|\le57/1000\). Put
\[
 L=[0,1/10],\qquad P=[11/50,9/20].
 \tag{1}
\]
Use the periodic continuous piecewise linear function
\[
 \rho(x)=
 \begin{cases}
 0,&0\le x\le1/10,\\
 \dfrac{25}{3}(x-1/10),&1/10\le x\le11/50,\\
 1,&11/50\le x\le9/20,\\
 20(1/2-x),&9/20\le x\le1/2,\\
 0,&1/2\le x\le1,
 \end{cases}
 \qquad
 H_j(x)=h_j^*\rho(x_{j-1})\rho(x_j)\rho(x_{j+1}).
 \tag{2}
\]
Repeated cyclic subscripts mean repeated factors. By the
[coupled contour theorem](research_mixed_coupled_outer_graph.md),
the full unaliased Laurent constant term equals its integral on
this graph with the exact Jacobian \(\det(I+iDH)\), and no added
current. The original scalar normalization is unchanged.

On \((L\cup P)^m\), every low coordinate and every plateau
coordinate adjacent to a low one has height zero. All other
plateau heights equal their original critical heights. The
Jacobian equals one almost everywhere on these boxes, since
\(\rho\) is constant on the interiors of both \(L\) and \(P\).
The general bound \(|\det(I+iDH)|<(18/5)^m\) also holds.

For each original block write
\[
 \Gamma_v(z)=\phi_v(r_v)+\phi_v'(r_v)\cdot(z-r_v),
 \tag{3}
\]
where \(\phi_v\) is the allocated conditional phase, with its
original half-factorial weights, and \(r_v\) is its actual
complex reference pair. The zero-lift critical equations give
\[
                       \Re\sum_v\Gamma_v=M .
 \tag{4}
\]
This cancellation retains all imaginary-height terms.

## 2. Uniform finite estimates for the three edge kinds

For an edge with one low and one plateau endpoint, both heights
are zero. If its low angle is in \([0,1/1000]\), the
[real zero collar](research_mixed_real_zero_collar.md)
gives an original raw-source gap \(3/50\), uniformly including
zero. If it is in \([1/1000,1/10]\), the
[coherent real one-small theorem](research_mixed_real_one_small_support.md)
applies on the fixed compact product with the other endpoint
in \(P\), giving gap \(1/20\). Taking the larger finite constants
therefore gives, for every \(LP\) or \(PL\) edge,
\[
 |\text{allocated original block}_v|
   \le C N^A e^{N(\Re\Gamma_v-1/20)} .
 \tag{5}
\]
There is no level-dependent lower cutoff in (5).

For an \(LL\) edge, both target heights are zero and both angles
belong to the closed interval \(L\). The
[both-low raw theorem](research_mixed_both_low_raw_support.md)
gives the weaker but zero-uniform bound
\[
 |\text{allocated original block}_v|
   \le C N^A e^{N(\Re\Gamma_v-1/100)} .
 \tag{6}
\]
The stronger compact coherent gap is not substituted at zero.

For a \(PP\) edge, both real parts lie in \(P\), while each
height is either its reference height or zero. The
[full matrix reset theorem](research_mixed_full_height_reset.md)
allows both real parts to readjust and gives
\[
 \Re\phi_v(z)-\Re\Gamma_v(z)
                 \le10\sum_{j\in v,\ {\rm reset}}(h_j^*)^2.
 \tag{7}
\]
Every type-four target here belongs to the fixed compact set
\(P+i[-.057,0]\), on which \(\nu=-\Re g>0\).
The [relative Fourier-weight theorem](research_mixed_fourier_weight_continuation.md),
Theorem 1, therefore applies to every such weight, including
weights at reset real coordinates. Combined with the full
right-square conditional packet, it gives an upper bound at
the exact allocated rate, with only a polynomial factor:
\[
 |\text{allocated original block}_v|
 \le C N^A
  \exp N\left(\Re\Gamma_v+
             10\sum_{j\in v,\ {\rm reset}}(h_j^*)^2\right).
 \tag{8}
\]
No per-block positive rate tolerance is needed in (8).
In particular unchanged \(PP\) edges cost zero rate.
The interval stops at .45, so no Fourier forcing tie at .5
is silently treated as a relative approximation.

All bounds retain the complete finite kernels and the actual
Fourier polynomials. The allocated half-moduli recombine into
the original integer powers when the edges are multiplied.
Only the unaliased term is used at nonzero heights.

## 3. Arbitrary cyclic clusters, including lengths one and two

Let \(n_{LP}\) count all \(LP\) and \(PL\) edges with their
original multiplicities, let \(n_{LL}\) count \(LL\) edges,
and let \(n_G=n_{LP}+n_{LL}\). A reset plateau vertex has
\(k=1\) or \(2\) low incidences. Its number of nongapped \(PP\)
incidences is \(2-k\le k\). Thus the sum of all reset costs in
(8) is at most
\[
                         10(.057)^2\,n_{LP}.
 \tag{9}
\]
This is incidence charging, not an enumeration of word lengths.
A length-two mixed low/plateau cycle has two low incidences at
its plateau vertex and no \(PP\) cost. A length-one low cycle
has one \(LL\) edge and no plateau vertex. All-low cycles also
have no reset cost.

Multiplying (5), (6) and (8), and using (4), proves the finite
whole-density bound
\[
 \begin{split}
 |\text{original normalized unaliased density}|
 &\le C N^A
 \exp N\left[
    M-\left(\frac1{20}-10(.057)^2\right)n_{LP}
       -\frac1{100}n_{LL}\right]\\
 &\le C N^A e^{N(M-n_G/100)}.
 \end{split}
 \tag{10}
\]
The exact first coefficient is
\(1/20-10(.057)^2=1751/100000>1/100\).
Constants and the harmless polynomial power may depend on the
fixed word, but not on the target angles or their distance to zero.

**Theorem 1.** On the graph (2), every part of
\((L\cup P)^m\) containing at least one low coordinate has
an exponentially smaller absolute unaliased integral, uniformly
through all zero angles:
\[
 \int_{(L\cup P)^m\setminus P^m}
       |\text{original unaliased density}\,\det(I+iDH)|\,dx
                  \le C N^A e^{N(M-1/100)}.
 \tag{11}
\]
Indeed \(n_G\ge1\) there. There are only finitely many boxes for
the fixed word, and the graph Jacobian has no exponential cost.
Both integer-level parities are included.

## 4. The retained contribution and remaining regions

On \(P^m\), (2) is exactly the original constant-height
unselected plateau and its Jacobian is one. The
[whole plateau theorem](research_mixed_plateau_accretivity.md),
equation (18), already gives its original critical exponential,
nonzero coefficient, Gaussian branch and level power \(N^0\).
By (11), its asymptotic is unchanged when the unaliased contribution
over all of \((L\cup P)^m\) on this coupled graph is included.
This is a contribution to the original Laurent integral, with
the original scalar retained; it is not a replacement source.

The coupled graph also resets neighbors of right-half coordinates.
Consequently prior right-half supporting-plane bounds cannot be
imported onto it without checking the new heights. Coordinates
in \((.1,.22)\) and \((.45,1]\), and selected outer aliases,
remain outside the assembly proved here. No complete cyclic
asymptotic, ordinary-boundary filling theorem, or knot-volume
conclusion is asserted.

## 5. Reproduction

    python3 experiments/check_mixed_uniform_low_plateau_clusters.py

The checker validates the current finite-source inputs, the
cutoff/Jacobian arithmetic and exact loss budget, and the original
incidence charging for all low/plateau patterns through length ten.
The degree-two incidence argument proves the result for every
fixed cyclic length.
