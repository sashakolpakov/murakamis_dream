# A quantitative volume gap for actual long-filled groups

Research note, 18 November 2026.

The full group relation of a Dehn filling forces every nearby centered
primitive charge to be a nonzero integer. Consequently the geometric
charge comparison applies to every other admitted representation of the
filled group, without matching a Fourier label to that centered charge.
This is a statement about classical representations, not source cycles.

## 1. Proof sources, normalization, and theorem

The complete proof sources are:

* **G**, [A uniform representation-volume gap along centered long cone
  paths](research_centered_long_cone_representation_volume_gap.md).
* **F**, [A finite positive certificate supplies every sufficiently long
  filling branch](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/finite_geometric_certificate_uniform_filling_existence.md).

Fix the marked complete hyperbolic core \(M\), its positive complete
certificate, and its positively oriented primitive cusp bases
\((\mu_i,\lambda_i)\), as in these sources. A fixed earlier short
partial filling may already be part of \(M\).
Fill a nonempty subset \(I\) along primitive slopes
\[
 \alpha_i=\mu_i^{a_i}\lambda_i^{b_i},\qquad
 \gcd(a_i,b_i)=1,\qquad
 \ell_i=(a_i^2+b_i^2)^{1/2}.
 \tag{1}
\]
Write \(M(\sigma)\) for the actual marked filling and
\(\pi:\pi_1M\twoheadrightarrow\pi_1M(\sigma)\) for its quotient map.
All remaining cusps, including every unfilled physical main cusp, are
retained.

An admitted representation in this note is
\[
 \rho:\pi_1M(\sigma)\longrightarrow\mathrm{PSL}_2(\mathbb C)
 \tag{2}
\]
whose image on every remaining cusp is boundary-parabolic, with the
trivial image allowed. Use the signed representation volume normalized
by the same oriented fundamental class as G and F. Section 2 checks its
equality with the normalized volume of the core pullback
\(\widehat\rho=\rho\circ\pi\).

The parabolic condition on the remaining cusps is substantive. It is
what fixes their centered peripheral coordinates to zero near complete
holonomy. No uniform gap over varying nonparabolic boundary conditions
is asserted. If all cusps are filled, this condition is empty.

**Theorem.** There are constants \(L_*,\delta,c_1>0\), depending only
on the fixed marked core and certificate, such that for every primitive
slope tuple with \(\ell_{\min}>L_*\), the filling \(M(\sigma)\) is
the actual oriented hyperbolic filling supplied by F. Let
\(\rho_{\mathrm{hyp},\sigma}\) be its oriented projective holonomy.
Every admitted representation not conjugate to it satisfies
\[
 \operatorname{Vol}_{M(\sigma)}(\rho)
 \le
 \operatorname{Vol}(M(\sigma))
 -
 \min\left\{\frac{\delta}{2},
            \frac{3c_1}{\ell_{\max}^2}\right\},
 \qquad
 \ell_{\max}=\max_{i\in I}\ell_i.
 \tag{3}
\]
One choice works for all subsets, signs and independently unequal long
slope lengths. The comparison is between underlying projective
conjugacy classes. Central lifts and different source decorations of
the same projective representation are not separated by volume.

## 2. Pullback volume and cyclic filled peripheral images

Primitivity in (1) implies
\(\mathbb Z^2/\langle(a_i,b_i)\rangle\cong\mathbb Z\).
Therefore the image of the \(i\)-th filled peripheral group under
\(\widehat\rho\) is cyclic. In particular it is trivial, parabolic, or
fixes both endpoints of an axis individually. There is no peripheral
endpoint-interchanging group hidden in this assertion.
Together with the admitted unfilled cusps, these are precisely the
peripheral types used by the core volume comparison in G.

Here is a map-level verification of the normalization under filling.
On a filled solid torus, use coordinates \((d,t)\in D^2\times\mathbb R\)
on its universal cover, with \(t\mapsto t+1\) representing the core
generator \(g\). Choose a \(g\)-equivariant curve
\(\gamma:\mathbb R\to\mathbb H^3\) and put
\[
                    \mathcal D(d,t)=\gamma(t).
 \tag{4}
\]
For a loxodromic \(g\), take its axis with the appropriate translation
speed. For an elliptic \(g\), take a constant point on its axis.
For a parabolic \(g\), conjugate it to \(w\mapsto w+b\) and use
\(\gamma(t)=(tb,1)\) in upper-half-space coordinates.
For the identity take a constant curve. These maps are equivariant
for the actual cyclic peripheral quotient and have differential
rank at most one. Their volume integrals are zero.

Prescribe the same maps on the bounding tori of a compact truncation
of \(M\), independent of the meridional coordinate. An equivariant
map on the remaining compact core with these boundary values exists
by extending over a lifted finite cell decomposition: the target
\(\mathbb H^3\) is contractible, and each cell extension is propagated
equivariantly. Smooth it relative to the fixed collars.
Keep identical admissible maps on all unfilled cusps in the two
constructions.

For the core volume, replace each solid torus by a cusp tail. In the
axis case the tail can be kept in that same axis. In the parabolic
case use \((tb,e^s)\), with the cusp-depth variable \(s\ge0\); its
image lies in the vertical hyperbolic plane over the line
\(\mathbb R b\). The trivial case uses a ray. Each such tail has
rank at most two and zero three-volume, and matches (4) at its
initial torus. These are the cyclic instances of the axis/parabolic
cusp models defining the volume in G. Changing the axis-depth
parametrization, or comparing the displayed parabolic tail with its
conical ideal end, remains in the same axis or plane; the comparison
homotopy has zero three-volume as well.

The compact-core integrals and all unfilled ends are thus identical,
and the added pieces contribute zero. With the retained orientation,
\[
          \operatorname{Vol}_{M(\sigma)}(\rho)
                 =\operatorname{Vol}_M(\widehat\rho).
 \tag{5}
\]
This uses the full cyclic quotient at the filled tori. An equation for
peripheral eigenvalues alone would not supply the solid-torus map.

## 3. The full slope relation forces a nonzero centered charge

Use the fixed conjugacy-invariant complete-holonomy neighborhood
\(\mathcal U\) from G, shrinking it if necessary as in its Section 4.
Every admitted pullback in \(\mathcal U\), with any retained peripheral
fixed flags, lies in the actual positive decorated gluing chart.
Its centered similarity logarithms satisfy
\[
              V_i=U_i\tau_i(U),\qquad
              \Im\tau_i(U)\ge m>0.
 \tag{6}
\]
For unfilled cusps, boundary-parabolicity gives their centered
\(U_i=V_i=0\).

At a filled cusp the full projective matrix relation is
\[
                     \widehat\rho(\alpha_i)=I.
 \tag{7}
\]
Taking its similarity multiplier on the retained fixed flag gives
\[
       a_iU_i+b_iV_i=2\pi i q_i,\qquad q_i\in\mathbb Z.
 \tag{8}
\]
Here \(U_i,V_i\) themselves remain centered; (8) is not obtained by
choosing their deck translates.

Suppose \(q_i=0\). The denominator estimate in F gives
\[
       |a_i+b_i\tau_i(U)|\ge c_0\ell_i>0.
 \tag{9}
\]
Equations (6), (8) imply \(U_i=V_i=0\).
In the moving selected-flag affine frame, F supplies the actual
commuting maps
\[
 \mu_i(w)=e^{U_i}w+B_i(U),\qquad
 \lambda_i(w)=e^{V_i}w+D_i(U),\qquad B_i(U)\ne0.
 \tag{10}
\]
Moreover, on \(U_i=0\),
\[
                         D_i/B_i=\tau_i(U).
 \tag{11}
\]
For completeness, differentiate the exact commuting identity
\((e^{U_i}-1)D_i=(e^{V_i}-1)B_i\) in the coordinate \(U_i\),
holding all other coordinates fixed, and set \(U_i=0\).
Since \(V_i=U_i\tau_i(U)\), this gives (11).

The slope map when \(U_i=V_i=0\) is therefore the translation
\[
       w\longmapsto
       w+a_iB_i+b_iD_i
       =w+B_i(a_i+b_i\tau_i(U)).
 \tag{12}
\]
Its translation is nonzero by (9)--(10), so it is not the identity.
This contradicts the full relation (7). We have proved
\[
                         q_i\in\mathbb Z\setminus\{0\}
                         \qquad(i\in I).
 \tag{13}
\]

If one starts with \(\mathrm{SL}_2\) data, projectivize while retaining
its actual central signs. A slope matrix \(+I\) or \(-I\) both give
(7); the nonidentity parabolic (12) gives neither. Thus the proof
does not presume an odd-only or an even-only charge congruence.
It also does not identify the integer \(q_i\) with a quantum Fourier
label. The full group relation is what excludes zero.

## 4. The gap for all admitted filled-group representations

Source G gives a fixed \(\delta>0\) such that every admitted core
representation outside \(\mathcal U\) has volume at most
\(\operatorname{Vol}(M)-\delta\).
Its long-slope threshold can be chosen so that
\[
 \operatorname{Vol}(M(\sigma))
                  >\operatorname{Vol}(M)-\delta/2.
 \tag{14}
\]
By (5), a filled-group representation whose pullback is outside
\(\mathcal U\) therefore has deficit greater than \(\delta/2\).

For a pullback in \(\mathcal U\), (13) places all its centered charges
in the nonzero integer set. G's neighborhood was chosen so that all
these charges lie in its larger box
\(|q_i|\le\rho_*\ell_i\). Its exact monotonicity estimate gives
\[
 \operatorname{Vol}(M(\sigma))
       -\operatorname{Vol}_M(\widehat\rho)
 \ge c_1\sum_{i\in I}\frac{q_i^2-1}{\ell_i^2},
 \qquad
 c_1=\frac{\pi^2m}{1+T^2}>0.
 \tag{15}
\]
If any \(|q_i|\ge2\), the right side is at least
\(3c_1/\ell_{\max}^2\).
If all \(|q_i|=1\), the independent flag-reversal and contraction
argument in G identifies the underlying pullback representation with
the unit-charge geometric one. Since \(\pi\) is surjective, a
conjugacy of these pullbacks is also a conjugacy of the representations
of \(\pi_1M(\sigma)\). Such a representation is the excluded
\(\rho_{\mathrm{hyp},\sigma}\).
Together with the outside-neighborhood case and (5), this proves (3).

## 5. Source scope

The theorem removes a classical charge-matching premise for
representations that already satisfy the actual filled-group relations.
It does not prove that every source critical configuration satisfies
those relations as matrices, or that its action has the required
representation-volume normalization. A peripheral exponential equation
alone still permits the nonidentity parabolic excluded in (12).

Nor does the theorem compare distinct source lifts of geometric
holonomy or determine their combined coefficient. Source boundary
currents, escaping decorations, the original highest-cut relative
cycle and its physical observation remain separate. No quantum lower
bound or noncancellation statement is inferred.

## Frozen proof-source pins

* G: research_centered_long_cone_representation_volume_gap.md,
  SHA256 5e68b3c689a8b85454ae256c3e298a412ddf9ff3ef52cfef5c836dace0da85d5.
* F: finite_geometric_certificate_uniform_filling_existence.md,
  SHA256 f3f78212e1f42f501593412a71c21590f24f8838f4add8abeb2f12534ad2b39b.
