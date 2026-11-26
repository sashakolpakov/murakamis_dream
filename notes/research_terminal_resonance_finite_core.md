# Finite minimal cores of signed terminal resonance

Private written corollary, 16 November 2026.

At fixed arity, the signed reciprocal resonance underlying the
terminal-product projection has only finitely many inclusion-minimal
cores. Every remaining factor belongs to a zero-sum complement.
That complement can have unbounded powers and an unbounded phase
denominator, so this is not a finite classification of the full
resonant assignments.

## 1. Minimal cores and a denominator bound

Fix \(\epsilon\in\{1,-1\}\). A tuple of nonzero integers
\((n_i)_{i\in I}\) is resonant if
\[
                         \sum_{i\in I}\frac1{n_i}=\epsilon.
 \tag{1}
\]
The indices remain labeled; repeated integer values are allowed.
A nonempty subset \(S\subset I\) is a minimal resonant core if
it has sum \(\epsilon\) and no proper subset has that sum.
The empty sum is zero.

**Theorem 1.** Every resonant tuple has a minimal resonant core.
For every such core, its complement has reciprocal sum zero.
If the core has length \(s\), order its entries so that
\[
                     m_1\le\cdots\le m_s,\qquad m_i=|n_i|.
 \tag{2}
\]
Then, with \(P_k=\prod_{i=1}^k m_i\) and \(P_0=1\),
\[
 \boxed{\quad m_{k+1}\le (s-k)P_k\quad(0\le k<s),\quad}
 \tag{3}
\]
and in particular
\[
           P_k\le s^{\,2^k-1},\qquad
           m_k\le s^{\,2^{k-1}}\quad(1\le k\le s).
 \tag{4}
\]
Thus the minimal cores of length at most any fixed \(r\) form
a finite set, up to permutation.

**Proof.**
Choose an inclusion-minimal subset among the finitely many
subsets with sum \(\epsilon\); the full index set is one.
Subtracting its sum from (1) proves the zero-sum complement.

A resonant tuple is minimal if and only if it has no nonempty
zero-sum subset. Indeed deleting a nonempty zero-sum subset
leaves a proper resonant subset; conversely, the complement
of a proper resonant subset is nonempty and has sum zero.
The full resonant set itself cannot be a zero-sum subset.

For \(0\le k<s\), the proper-prefix residual
\[
            R_k=\epsilon-\sum_{i=1}^k\frac1{n_i}
                    =\sum_{i=k+1}^s\frac1{n_i}
 \tag{5}
\]
is nonzero. Otherwise that prefix would be a proper resonant
subset. The number \(P_kR_k\) is an integer, since \(\epsilon\)
is an integer and every signed denominator in the prefix
divides \(P_k\). Hence
\[
           \frac1{P_k}\le |R_k|
               \le \sum_{i=k+1}^s\frac1{m_i}
               \le \frac{s-k}{m_{k+1}} .
 \tag{6}
\]
This proves (3), including \(m_1\le s\) when \(k=0\).
Now \(m_{k+1}\le sP_k\), so \(P_{k+1}\le sP_k^2\).
Induction from \(P_0=1\) gives the first bound in (4);
the second follows from \(m_k\le sP_{k-1}\).
The argument also covers \(s=1\), where \(m_1=1\).

For each fixed \(s\), (4) leaves finitely many positive
magnitude tuples, finitely many sign choices, and finitely
many permutations. Taking the finite union over \(s\le r\)
proves the last assertion. \(\square\)

## 2. Exact decomposition and what may remain unbounded

Set
\[
                           B_r=r^{\,2^{r-1}}\qquad(r\ge1).
 \tag{7}
\]
Every entry of every minimal core of length at most \(r\)
has magnitude at most \(B_r\), by (4).

**Corollary 2.** Up to permutation, every resonant tuple of
length at most \(r\) is the union of a member of a fixed
finite list of minimal cores and a tuple of reciprocal sum
zero, whose length is the remaining arity. Conversely,
every such union is resonant.

Every entry of magnitude greater than \(B_r\) belongs to
the zero-sum complement of every minimal core. Consequently,
from any fixed-arity sequence of resonant tuples with
unbounded maximum magnitude, one can extract a subsequence
with a fixed minimal core, up to permutation, and an
unbounded zero-sum complement.

**Proof.**
The decomposition and converse follow by adding or subtracting
the two sums. The bound (7) excludes any larger entry from a
minimal core. For the sequence assertion, first take a
subsequence whose maximum magnitude tends to infinity.
Choose a minimal core for each tuple. There are finitely
many possibilities, including their lengths and positions,
so one occurs on an infinite subsequence. The complement
on that subsequence must remain unbounded. \(\square\)

There is no uniqueness assertion: different minimal cores
can occur in the same tuple. The finite union in Corollary 2
need not be disjoint.

**Corollary 3.** At fixed arity, same-sign resonant tuples
form a finite set, up to permutation.

**Proof.**
A nonempty subset of same-sign nonzero reciprocals cannot
have sum zero. Hence every same-sign resonant tuple is
already minimal, and Theorem 1 applies. Its common sign
necessarily equals \(\epsilon\). \(\square\)

## 3. Application to the terminal projection and its limitation

For an actual outer unit turn \(U_\sigma\), the pinned
projective theorem identifies resonance as
\[
                           \sum_i1/n_i=-\sigma.
 \tag{8}
\]
Thus take \(\epsilon=-\sigma\) in Theorem 1. Every resonant
active subset has one of the finitely many cores above.
If no such core is present among the available powers,
then no active subset is resonant. The converse holds
because a core is itself an active subset. This is a
criterion for reciprocal resonance; the interior physical
projection also depends on the full active least common
multiple.

In fact, if \(L=\operatorname{lcm}_i|n_i|\), that theorem
gives the finite old-infinity limits
\[
                         2\cos(2\pi k/L),\qquad 0\le k<L,
 \tag{9}
\]
with an interior limit precisely when \(L\ge3\).
The bounded cores do not bound this \(L\).

For the general arithmetic family
\[
                         (\epsilon,p,-p),\qquad p\ge3,
 \tag{10}
\]
the singleton \((\epsilon)\) is a minimal core and
\((p,-p)\) is a zero-sum complement. The full tuple has
\(L=p\). Under \(U_{-\epsilon}\), (9) therefore has
unbounded denominators as \(p\) varies; the union of these
finite-limit sets is dense in \([-2,2]\), since rational
angles are dense and cosine is continuous. The singleton
core alone has \(L=1\) and no interior limit. Thus even the
interior projection condition cannot be checked by discarding
the complement.

Here “zero-sum complement” is only an arithmetic description.
No topological cancellation, operator cancellation, or
identification of distinct characteristic components is
asserted. In particular these bounds do not select any
actual source branch, establish its coefficient, prove
regularity of a cleared finite recurrence, or reduce the
remaining zero-sum-padded source problem to finitely many
integer assignments.
The bound \(B_r\) concerns denominators in minimal characteristic
resonances. It is not a sufficient Dehn-filling length or a
numerical threshold for a volume-conjecture theorem.

## 4. Coverage and direct source

A targeted local search for minimal resonant cores, signed
unit fractions and reciprocal zero-sum padding found no
existing version of the arithmetic bound. The proof in
Sections 1--2 is self-contained. Section 3 uses the complete
following source, read at its matching pin:

* [Projective resonance of terminal products](research_terminal_product_projective_resonance.md),
  SHA256 a648b644c5506e539d14fa715d61a3f680d7d53e48eec8efc1358b6ca047bf08:
  the actual inverse-pullback sign, phase grid and the distinction
  between characteristic support and source participation.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or compilation
was run. Frozen notes and public manuscripts are unchanged.
