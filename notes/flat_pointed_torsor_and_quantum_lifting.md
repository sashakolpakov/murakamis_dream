# A flat pointed torsor lifts; an etale classical optimizer need not

Independent proof and audit, 27 October 2026. This adds a constructive
comparison formula and a flatness criterion to
[whole cyclotomic reconstruction](whole_period_cyclotomic_rigidity.md).
It also gives rational quantum objects for which a unique reduced
classical pointed comparison fails to lift. Thus it distinguishes an
actual sufficient theorem from an implication that classical Rivin
rigidity alone does not supply.

The fixed-meridian Rees Poisson map and its new whole Heisenberg
primitive are checked in Section 5. Section 6 gives a concrete actual
crossing obstruction to a naive positive weighted-norm proof. None of
the statements below asserts the selected volume asymptotic.

## 1. A flat marked comparison has exactly one lift

Let \(R=k[[\epsilon]]\), with \(k\) of characteristic zero. Suppose a
whole, bounded algebraic comparison problem has been specified, including
its sources, cuts and lattice. Complete its comparison algebra at a
chosen classical point and call the resulting \(R\)-algebra \(B\).
Assume

\[
 B/\epsilon B=k,\qquad
 \bigcap_{n\geq 0}\epsilon^nB=0,
 \qquad \epsilon\text{ is a nonzero divisor on }B.       \tag{1}
\]

Then \(R\longrightarrow B\) is an isomorphism. In particular the marked
comparison exists uniquely to every formal quantum order.

Here is a direct proof. Given \(b\in B\), choose its residue \(c_0\in k\)
and write \(b=c_0+\epsilon b_1\). Repeat this for \(b_1\), obtaining
\[
 b-\sum_{j<n}c_j\epsilon^j\in\epsilon^nB.
\]
The element \(f=\sum c_j\epsilon^j\in R\) therefore maps to \(b\), by
separatedness. Thus \(R\to B\) is surjective. A nonzero element of its
kernel would be \(\epsilon^m\) times a unit, contradicting the last
condition of (1) and \(B/\epsilon B\ne0\). This proves the assertion.

Over this DVR, the last condition is exactly \(R\)-flatness. A
finite separable marked classical residue field is handled after its
specified unramified base extension. With a finite algebraic
presentation, this is a statement about its selected algebraic formal
germ; it does not assert that an arbitrary formal period is algebraic.

The same result retains several normal directions. Let \(R\) be any
complete Noetherian local ring, with maximal ideal \(\mathfrak m\)
and residue field \(k\). If \(B\) is separated for \(\mathfrak mB\),
is \(R\)-flat, and \(B/\mathfrak mB=k\) through the specified residue
map, then \(B=R\). Choose generators of \(\mathfrak m\) and repeat
the residue argument by total degree; completeness of \(R\) and
separatedness of \(B\) give \(B=R/I\), \(I\subseteq\mathfrak m\).
Flatness, applied to \(0\to I\to R\) and tensoring with \(B\),
forces \(I/I^2=0\). Since \(I\) is finitely generated and
\(I=I^2\subseteq\mathfrak mI\), Nakayama gives \(I=0\).
Thus quantum and meridian normals can be retained together.

There is a useful converse formulation. The first two conditions
already imply \(B=R/I\). If comparisons exist modulo \(\epsilon^n\) for
every \(n\), the maps \(R/I\to R/\epsilon^n\) give
\(I\subseteq(\epsilon^n)\) for all \(n\); hence \(I=0\).
No additional choice of compatible lifts is needed once the pointed
comparison is unique. Comparisons at several different cyclotomic
levels become such a test only after a fixed whole presentation and
the reconstruction hypotheses have been supplied.

This is a genuine existence theorem for a flat whole pointed comparison.
Flatness of the two objects separately is a different condition.

## 2. Cyclic pointing constructs the only possible comparison

Here the comparison need not be guessed. Let \(A\) be a coefficient
algebra with an automorphism \(\sigma\). Let \(V_i=A^r\) carry the
semilinear transport \(T_i(v)=A_i\sigma(v)\), source \(s_i\), and cut
\(\ell_i\), for \(i=1,2\). Form the cyclic matrices

\[
 V_i^{\mathrm{cyc}}=[s_i,T_i s_i,\ldots,T_i^{r-1}s_i].
\]

Assume their determinants are units on the marked lattice chart. Define

\[
 C=V_2^{\mathrm{cyc}}(V_1^{\mathrm{cyc}})^{-1},\qquad
 a_i=(V_i^{\mathrm{cyc}})^{-1}T_i^r s_i,\qquad
 m_i=\ell_i V_i^{\mathrm{cyc}}.                         \tag{2}
\]

Then \(C\) and its inverse are regular on that chart, and

\[
 CT_1=T_2C,\quad Cs_1=s_2,\quad\ell_2C=\ell_1
 \quad\Longleftrightarrow\quad
 a_1=a_2,\quad m_1=m_2.                            \tag{3}
\]

Moreover \(C\) is the only pointed transport comparison.

Indeed every such comparison must send each \(T_1^j s_1\) to
\(T_2^j s_2\), which forces (2). Its transport residual vanishes on
the first \(r-1\) cyclic vectors. On the last vector it vanishes exactly
when their last cyclic relations \(a_i\) agree. Equivalently,
\[
 A_i\sigma(V_i^{\mathrm{cyc}})=V_i^{\mathrm{cyc}}\operatorname{Comp}(a_i);
\]
substituting (2) proves the transport identity. The cut identity is
exactly equality of the two rows \(m_i\).

Consequently, near a regular cyclic classical comparison, its whole
comparison algebra is
\[
 B=R/I,\qquad
 I=(\text{entries of }a_1-a_2,\ m_1-m_2),            \tag{4}
\]
with additional supplied connection residuals included if required.
This makes the flatness defect an explicit finite obstruction ideal.
Classical agreement says only \(I\subseteq(\epsilon)\); flatness says
\(I=0\).

If the objects and these finitely many iterates have a fixed bounded
algebraic presentation, the
[cyclotomic jet theorem](whole_period_cyclotomic_rigidity.md)
tests the residuals in (3), after denominators and algebraic norms
are handled in the stated lattice. Thus a regular cyclic source
gives a canonical comparison and a finite exact certificate.
There is no unknown unbounded family of levelwise gauges in this
construction.

The hypotheses are substantive: the rank must be fixed for a uniform
test, both cyclic determinants must be units, and the whole transports
and pointings must already exist. Generic cyclicity away from a
source boundary does not imply these unit conditions. The full
finite \(N\)-dimensional module and a rank-one local geometric block
are also not interchangeable objects.

For compatible differential period connections, horizontality can
follow from this uniqueness. If the connections commute with transport,
and the two source connection laws agree under \(C\), then
\(E=\nabla_2C-C\nabla_1\) commutes with transport and kills the source.
It kills every cyclic vector, so \(E=0\). For the mixed quantum and
meridian law, the extra meridian intertwining in
[the whole comparison theorem, Section 5](whole_period_cyclotomic_rigidity.md)
is required. This argument does not construct either connection.

## 3. Two explicit failures of classical-to-quantum lifting

### Flat objects with a nonflat pointed comparison

Take rank-one free \(R\)-modules, with transports \(T_1=1\) and
\(T_2=1+\epsilon\), and sources \(s_1=s_2=1\). Both objects are flat.
A source-preserving comparison is forced to be \(C=1\), so its remaining
equation is \(\epsilon=0\). Its comparison algebra is \(R/(\epsilon)\).

There is one reduced classical pointed comparison and no quantum lift.
The same example works for meridian-difference transports
\(T_1=\sigma\), \(T_2=(1+\epsilon)\sigma\) over
\(k(Y)[[\epsilon]]\), with \(\sigma(Y)=e^\epsilon Y\).
It has the same classical graph \(L=1\), etale over \(Y\).
Thus etaleness of that graph and flatness of the objects do not imply
flatness of their pointed comparison.

### Even the unpointed algebraic gauge can fail

Put \(Q=e^\epsilon\), \(\sigma(Y)=QY\), and compare the rank-one
transport multipliers
\[
 a_1(Q,Y)=1,\qquad a_2(Q,Y)=1+\frac{Q-1}{Y}.        \tag{5}
\]
They are rational whole functions, regular formally at \(Q=1\), with
the same classical etale graph \(L=1\). An algebraic formal unit
solving the gauge equation \(\sigma g=a_2g\), with leading term \(g_0\),
would satisfy
\[
 Y\partial_Yg_0=g_0/Y,\qquad
 d\log g_0=dY/Y^2.                               \tag{6}
\]
This is impossible on every finite algebraic cover. A logarithmic
derivative of an algebraic meromorphic function has only simple
poles. At a place \(Y=t^e\), the right side of (6) has pole order
\(e+1>1\). The analytic solution \(g_0=\exp(-1/Y)\) demonstrates
precisely the excluded irregularity.

Multiplying both multipliers by any common nonzero rational
\(a_0(Y)\) gives the same failure over the graph \(L=a_0(Y)\).
The issue is therefore not the particular constant classical graph.
At first quantum order, the difference of subprincipal transport
defines the necessary logarithmic connection (6); classical
etaleness does not trivialize that connection.

The full cyclic norm detects the failure exactly:
\[
 \prod_{j=0}^{N-1}a_2(Q_N,Q_N^jY)
   =1-\left(-\frac{Q_N-1}{Y}\right)^N\ne1.         \tag{7}
\]
For fixed \(Y\ne0\), its difference from one is smaller than every
power of \(1/N\). Thus even this rational transport produces a
curvature error invisible to its asymptotic \(1/N\) expansion.
It is visible to the *exact* whole cyclotomic test.

In the opposite direction, the independently proved
[full rank-one descent theorem](full_rank_one_cyclotomic_descent.md)
does give a positive result: a comparison multiplier in
\(\mathbb Q(Q,Y)^*\), with exact whole norm one at every sufficiently
large root, has one rational gauge. Other coefficient fields require
the whole-root marking in that theorem. Its source anchor fixes the residual scalar,
provided the gauge and inverse are regular on the prescribed
source lattice. Equations (5)--(7) explain why the whole norm
hypothesis cannot be replaced by a classical optimizer or an
all-orders asymptotic norm identity.

## 4. The actual Rees source has a concrete regular-lifting obstruction

The
[actual Rees construction](irregular_rees_full_cyclic_module.md)
has block clock \(D_Zf(u)=f(Zu)\), \(Z=Q^N\), and
\[
 G^{-1}D_ZG=e^{u/N}D_Z,\qquad
 G=e^{u/[N(Z-1)]}.                               \tag{8}
\]
The original vacuum is fixed by \(D_Z\).

There is no regular clock intertwiner sending this vacuum to a
nonzero regular limiting vector. For such an intertwiner \(C\),
applying (8) to the vacuum and reducing at \(Z=1\) would give
\[
 (e^{u/N}-1)\,C_0(1)=0
 \quad\text{in }k[[u]],
\]
so \(C_0(1)=0\). Allowing mixing among head clocks does not help:
the equations become
\((Q_N^j e^{u/N}-1)f_j(u)=0\), and each factor is a nonzero
divisor. The exact irregular gauge instead sends the source to
\(e^{-u/[N(Z-1)]}\), as retained in that note.

This is not a claim that two identical whole-center families are
inequivalent: their normal central characters differ, and the
source gauge is explicitly irregular. It is a concrete warning
that a regular generator-module limit and matching closed-point
data do not produce a regular pointed lift through the source
boundary. The newly regular Rees module has not silently made
the comparison algebra flat.

## 5. Independent check of the Rees Poisson and period formulas

The new Sections 6--7 of
[the Rees module note](irregular_rees_full_cyclic_module.md) are sound.
With \(d=N(Q^N-1)\),
\[
 (Q^{N^2}-1)/d\longrightarrow1,\qquad
 (Q^{-N^2}-1)/d\longrightarrow-1.
\]
They give \(\{k,e\}=ke,\ \{k,f\}=-kf\); the actual universal
Casimir gives \(\{e,f\}=k^{-1}-k\). For \(\{p,u\}=1\),
\[
 U=e^{up},\quad k=\gamma M^N/U,\quad
 e=p\gamma(M^N/U-M^{-N}),\quad f=(1-U)/p
\]
has exactly these brackets, and
\[
 du\wedge dp=d\log U\wedge d\log p
            =-d\log k\wedge d\log e.
\]
At \(M=1\), \(v=1/p,w=e/\gamma\) gives
\(\Omega=dw\wedge dv/(1+wv)\), with the stated regular E-wrap
limit \(w/N\). The fixed-root normal \(d\) remains distinct from
the physical \(2\pi i/N\).

The new
[whole Gauss period transgression](rees_gauss_period_transgression.md)
also checks. For \(B=M^N,t=U/B^2\), its four period coordinates
satisfy the flat algebraic connection
\[
 d\mu=dB/B,\quad d\xi=dt/t,\quad
 d\ell=-dt/(1-t),\quad dH=\xi\,d\ell.
\]
This is a fixed Heisenberg times additive-logarithm torsor, before
level restriction. With \(x=\xi+2\mu\),
\[
 W=H+2\mu\ell-x^2/2,\qquad
 \theta_{\mathrm{Gauss}}-\theta_{\mathrm{source}}
     =dW+(x-2\ell)d\mu .
\]
Both the sign and the peripheral correction follow by direct
differentiation. The resolved \(M=1\) primitives have exterior
derivative \(dw\wedge dv/(1+wv)\); their difference is the
derivative of the stated regular \(W-\operatorname{Li}_2(1)\).
This is an actual local period connection, not merely matching
symplectic dimensions. Its existence does not by itself prove
a flat pointed comparison with the irregular selected source.

## 6. Scalarity does not make a positive weighted norm sharp

There is an actual crossing example, requiring no speculative
analytic sector. Close one leg of a positive checked crossing at
complete color \(M=1\). This is the framed unknot kink. Write
\[
 Q=e^{2\pi i/N},\quad q=e^{\pi i/N},\quad x=-q^{-1},
 \qquad P_a(Q)=(Q;Q)_a.
\]
At fixed cut index \(a\), closure forces the crossing index
\(k=a-b\), \(0\le b\le a\). Substituting the actual balanced
crossing and pivot gives the diagonal cut terms
\[
 x^{1-N}\,
 Q^{b^2}\frac{P_a(Q)^2}{P_b(Q)^2P_{a-b}(Q)}.       \tag{9}
\]
For clarity, the unsubstituted crossing coefficient is
\[
 (-1)^kq^{k^2}
 \left[\prod_{j=b+1}^{a}(Q^{-j}-1)\right]
 {a\brack k}_Q\,
 x^{-a-b}Q^{ab}\,
 (xQ^{-b})^{1-N};
\]
elementary cancellation gives (9), including its phase.

The exact finite identity
\[
 \sum_{b=0}^{a}
 Q^{b^2}\frac{P_a(Q)^2}{P_b(Q)^2P_{a-b}(Q)}=1      \tag{10}
\]
can be proved without importing a knot formula. Partitions with
largest part at most \(a\) have generating function \(1/P_a\).
Separate them by their Durfee square of size \(b\). Its weight is
\(Q^{b^2}\); the part below it has generating function \(1/P_b\),
and the rectangle to its right has generating polynomial
\({a\brack b}_Q=P_a/(P_bP_{a-b})\).
This proves (10) as a formal rational identity, hence at every
root with \(a<N\). The exact kink scalar is \(x^{1-N}\), of
modulus one.

Nevertheless, if \(4\mid N\), \(a=N/2,b=N/4\), the modulus of
this one closed term is
\[
 \frac{P(N/2)^2}{P(N/4)^3},\qquad
 P(m)=\prod_{r=1}^{m}2\sin(\pi r/N).
\]
The integrable logarithmic Riemann sum gives
\[
 \lim_{4\mid N\to\infty}\frac1N\log|\text{term}|
  =\frac{3\,G}{2\pi}>0,                         \tag{11}
\]
where \(G=\sum_{j\ge0}(-1)^j/(2j+1)^2\).
Indeed \(\int_0^{1/2}\log(2\sin\pi t)\,dt=0\) and
\(\int_0^{1/4}\log(2\sin\pi t)\,dt=-G/(2\pi)\).

Every internal diagonal basis weight cancels around this closed
term; a normalized cut basis vector and its dual cancel their
external weight too. Thus any bound obtained by replacing all
entries by absolute values, including products of induced
coordinate weighted norms, is at least this exponentially large
term. It cannot be sharp for the unit scalar (10).

This does not rule out a specially chosen wavepacket or a
phase-sensitive propagation theorem. For this kink, the cut
\(a=0\) is already cancellation-free. It does show why scalarity
alone and strict concavity of a classical shape functional do
not supply the required sharp positive norm for an arbitrary
normalized source. A useful coherent-state argument must prove
its phase-sensitive propagation and stability through the
actual crossings and caps, rather than infer them from the
algebraic optimizer.

## 7. The concrete whole-torsor task

There is now a precise positive route: construct the two whole
pointed objects, prove regular cyclicity on their marked lattices,
and evaluate the finite residuals (3). A flat comparison algebra,
or sufficiently deep exact cyclotomic tests in the fixed
presentation, then gives the unique comparison; a compatible
marked connection gives horizontality.

Rivin rigidity supplies the unique algebraic geometric place.
The new Rees--Gauss identity supplies a fixed algebraic period
connection on actual source coordinates. Neither presently
implies the comparison-flatness or removes the irregular
projectors. Those are explicit equations and source conditions
to prove. Even after that algebraic comparison, the physical
large-level norm requires a calibrated nonzero selected
contribution and its growth estimate.
