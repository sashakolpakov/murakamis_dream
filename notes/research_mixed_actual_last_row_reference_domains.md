# Actual reference domains for ordinary open-word last rows

Research reduction, 5 November 2026. The actual external legs of an
ordinary conditional factor belong to four explicit clipped disks.
Their roles determine which product is needed, including the
two-attached-input case at length three. The inherited reference
boundary principle reduces a uniform last-row comparison to a finite
family of three-real-dimensional boundaries. No sign of that
comparison on the whole family is asserted here.

## 1. Four compact geometric enclosures

Let \(P_3,P_4\) be the closed reduced disks in the
[complete conditional source theorem](research_mixed_reduced_disk_conditional_packets.md).
Define the ordinary-leg enclosures
\[
 \begin{split}
 O_3&=P_3\cap\{-13/200\le\Im z\le17/250\},\\
 O_4&=P_4\cap\{-51/500\le\Im z\le-1/1000\},
 \end{split}
 \tag{1}
\]
and the attached-endpoint enclosures
\[
 \begin{split}
 A_3&=P_3\cap\bigl([139/500,391/1000]
                              +i[-9/125,21/1000]\bigr),\\
 A_4&=P_4\cap\bigl([123/500,7/20]
                              +i[-27/250,-1/50]\bigr).
 \end{split}
 \tag{2}
\]
All four sets are compact convex sets with nonempty interior and
are strictly inside the old typed input disks \(D_3,D_4\).
The actual ordinary inputs lie strictly inside (1), by the whole-map
[ordinary image bounds](research_mixed_cyclic_critical_height_bounds.md)
and their [open-word inheritance](research_mixed_open_local_factor_coverage.md).
The actual attached inputs lie strictly inside (2), by the same
reduced-disk extraction and the
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md).
The real constraints in (2) are essential; a union of height
intervals alone is a larger domain.

## 2. Which product occurs at each ordinary factor

For an open word of length \(m\), use its original legs
\((s_j,t_j)\). The private legs are \(s_1,t_m\), while
the attached endpoint legs are \(t_1,s_m\). An ordinary
conditional factor occurs at
\[
 2\le j\le m-1,\qquad
 a=t_{j-1},\quad c=s_{j+1},\quad(s,b)=(s_j,t_j).
 \tag{3}
\]
Its two original equations are the ordinary two-leg block equations
with external parameters \((a,c)\). The corresponding conditional
factor uses the orientation \((s;a,b)\), with \(b\) an output
of this same map, not an independently chosen input.

The external roles are exactly as follows.

| Word length and ordinary vertex | Left external role | Right external role |
|---|---|---|
| \(m=3,j=2\) | Attached | Attached |
| \(m\ge4,j=2\) | Attached | Ordinary |
| \(m\ge4,j=m-1\) | Ordinary | Attached |
| \(m\ge5,3\le j\le m-2\) | Ordinary | Ordinary |

The type of each external leg is its own neighboring vertex type.
No private endpoint leg is an external parameter in (3). There
are no ordinary factors of this kind at \(m=1,2\). In particular
the terminal conditional factor, whose retained argument is the
private \(t_m\), remains a separate endpoint-map problem.

For example, at \(m=3\) the required enclosure is
\(A_{n_1}\times A_{n_3}\), with own type \(n_2\).
The endpoint equations further correlate these two inputs. Using
their full independent product is a sufficient enclosure, not an
assertion that all of that product is realized by open words.
The same distinction applies to every row of the table.

## 3. A finite ordinary-boundary family

Choose a product \(K=K_L\times K_R\), where each factor
is one of the four sets (1)--(2), with the roles prescribed above.
The original two-leg branch is holomorphic on a neighborhood of
\(K\), since \(K\) is contained in its previously proved
reduced-disk product. Write the own type as \(3+\epsilon\),
the left external type as \(3+\eta\), and the right external
type as \(3+\nu\). The allocated conditional phase is
\[
 \phi(a,b)=Q_\epsilon(s;a,b)
             -(1+\eta/2)g(a)-(1+\epsilon/2)g(b).
 \tag{4}
\]
The type \(\nu\) affects the parameter domain and the reference
map. It does not replace the own flag \(\epsilon\) in the
second halfweight or in the index equation.

For fixed target real parts \(X=(x,z)\in I^2\),
\(I=[11/50,9/20]\), define the exact last-row deficit
\[
 D(a,c;X)=E_1(x,z)-\Re\phi(a,b)
 -\Re\phi_a(a,b)(x-\Re a)-\Re\phi_b(a,b)(z-\Re b)
 +\kappa_0\bigl((x-\Re a)^2+(z-\Re b)^2\bigr),
 \quad \kappa_0=\frac1{2500000}.
 \tag{5}
\]
Here \(b=b(a,c)\), both target heights equal their reference
heights, and \(E_1\) retains the complete revived carrier and
the two prescribed factorial halfweights from the
[endpoint formula](research_mixed_horizontal_revived_endpoint.md).
The maximum over the four carrier branches is retained even when
a height is zero.

**Proposition.** On each product \(K\),
\[
 \max_{(a,c)\in K,\ X\in I^2}D(a,c;X)
 \le\max\left\{-\frac1{1000},
       \max_{(a,c)\in\partial K,\ X\in I^2}D(a,c;X)\right\}.
 \tag{6}
\]

*Proof.* The original reduced source theorem supplies the strict
matched entropy gap \(1/1000\), including every revived carrier.
Its original root branch and conditional Hessian are unchanged on
the smaller set \(K\). The map \((a,c)\mapsto(a,b(a,c))\)
is locally open, since its second-coordinate derivative is nonzero
as proved in that theorem. Every point of \(\operatorname{int}K\)
therefore admits the independent small real variations used by
the [reference-boundary principle](research_mixed_horizontal_tail_reference_boundary.md).
The strict horizontal Hessian bound there exceeds \(2\kappa_0\).
An interior maximizing reference with deficit greater than
\(-1/1000\) would consequently have both target real parts equal
to the reference real parts, where the matched gap contradicts
that value. Compactness gives (6).
The argument fixes the target and a maximizing carrier branch;
it requires no differentiation of their maxima. \(\square\)

Each boundary has a simple finite description. For \(O_3,O_4\),
it consists of the portions of the original circle inside the height
strip, together with the two horizontal clipping chords. For
\(A_3,A_4\), use the portions of the original circle inside the
rectangle and the portions of its four rectangle edges inside the
disk. Every chord endpoint is obtained by intersecting a rational
horizontal or vertical line with the rational-center circle, so its
coordinates are rational numbers and square roots of positive
rationals. Coincident endpoints may be retained more than once.

In particular
\[
 \partial K=(\partial K_L\times K_R)
                \cup(K_L\times\partial K_R)
 \tag{7}
\]
is a finite union of a one-real-parameter line or circle piece times
a two-real-parameter clipped disk. A certificate may cover a full
circle and discard the parts rigorously outside its clipping
rectangle; it must also include the new straight chords. Checking
only the old two-circle distinguished boundary would omit both
disk interiors in (7) and all clipping chords.

There are four domain labels \(O_3,O_4,A_3,A_4\). For each own
type, ten unordered pairs of these labels suffice if both original
conditional orientations are retained. Thus twenty typed products
cover all thirty-two ordered type/role cases. This is only finite
enumeration of sufficient domains; no sign check on those products
has been promoted to a theorem here.

The [untrimmed auxiliary obstruction](research_mixed_last_row_auxiliary_obstruction.md)
does not belong to any relevant product (1)--(2). Its exclusion does
not prove the opposite inequality on the clipped domains. A pilot
or a complete future certificate must retain the output correlation
\(b=b(a,c)\), the original logarithmic lift and the physical
halfweight allocation in (4)--(5). The algebraic own-root formulas
may simplify evaluation, but they do not authorize replacing the
same original roots by independent boxes.
