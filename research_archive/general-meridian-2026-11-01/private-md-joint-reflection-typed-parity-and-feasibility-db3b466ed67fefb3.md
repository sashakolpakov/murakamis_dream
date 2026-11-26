# Two preliminary facts for joint boundary reflection

Private note, 1 November 2026. The action inequality remains open here.

## 1. The reflected boundary is feasible

Let the marked covariant labels satisfy \(z_i\in[1/2,1]\), with at
most one marked incidence at each actual whole product hub. Write
\(r_i=1-z_i\in[0,1/2]\). Assign half to every other physical
internal edge and every ordinary leaf incidence. At each hub of full
valence \(D\ge3\), all pair sums are at most one and the total sum
is at least one. These are exactly the closed whole-hub support
conditions. The fixed-association interval lemma then supplies all
hidden unturned wires. Thus the reflected vector is feasible,
independently of whether the original vector was feasible.

If every \(r_i>0\), choose the free physical labels to be
\(1/2-\epsilon\), with one sufficiently small positive \(\epsilon\).
At a marked trivalent hub the total is
\(1+r_i-2\epsilon>1\); at higher-valence or unmarked hubs the
total also stays above one. Every pair sum is strictly below one.
This constructs a strict reflected state in every original binary
resolution. The case of a zero reflected mark is covered by closed
support and continuity.

## 2. Marked constant vertices need not have the same tree parity

Put \(A=V_x\otimes V_y\) and \(B=V_y\otimes V_x\). The six
actual quarter-turn types include
\[
\begin{array}{rcl}
 \operatorname{End}(A)&\longrightarrow&\operatorname{End}(B),\\
 \operatorname{End}(B)&\longrightarrow&\operatorname{End}(A),\\
 \operatorname{Hom}(A,B)&\longrightarrow&
                         \operatorname{End}(V_x\otimes V_x),\\
 \operatorname{Hom}(B,A)&\longrightarrow&
                         \operatorname{End}(V_y\otimes V_y).
\end{array}
\tag{1}
\]
The first two arrows stay in a constant opposite-color quotient; the
last two lead to a moving equal-color quotient.

Take two old constant trivalent hubs joined by the first physical
turn in (1). At the first hub, use an \(\operatorname{End}(A)\)
incidence for this internal edge and the other two incidences of
types \(\operatorname{Hom}(A,B)\) and
\(\operatorname{Hom}(B,A)\). Their compatible cyclic product is an
endomorphism of \(A\). Designate one Hom incidence as marked and
the other as an ordinary leaf. At the second hub use the reversed
orders: the internal incidence is \(\operatorname{End}(B)\), and
its two other incidences are \(\operatorname{Hom}(B,A)\) and
\(\operatorname{Hom}(A,B)\). Its compatible cyclic product is an
endomorphism of \(B\).

Each marked Hom incidence can be joined by its physical turn to a
moving equal-color hub, by the last two arrows in (1). Each ordinary
Hom leaf is also a legitimate turned integral crossing: it is the
turn of an equal-color crossing with the corresponding order. This
produces the typed pattern
\[
  \text{moving}\;--\;\text{constant}\;--\;
  \text{constant}\;--\;\text{moving},
\tag{2}
\]
with one ordinary mixed-Hom leaf at each middle vertex. All three
displayed connections are physical quarter-turns. Scalar carriers
are the prescribed ones and do not change these domains and
codomains.

The two marked old vertices are adjacent and hence have opposite
parity in the bipartition of the old region. A whole constant
product hub does not have one incidence type which can be iterated
uniformly around all of its other incidences: compatible products
may contain both opposite-End and mixed-Hom factors. Therefore the
four-cycle for an individual turn does not imply that all constant
vertices adjacent to moving vertices lie in one graph bipartition.

This is a typed local construction, not an assertion that every
choice of exterior closures is a knot. The domains and ordinary
leaf types required by the proposed old-region pressure comparison
are already realized here, so a same-bipartition restriction cannot
be imposed on those regions from the six-type turn table alone.
