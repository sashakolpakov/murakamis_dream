# A quantitative Schur lemma for the original head and its marked cut

23 November 2026. Research note. The manuscripts and earlier final
notes remain unchanged.

The original complete head admits a polynomial quantitative Schur
lemma. Two of its actual generators control the distance of an
arbitrary matrix from a scalar matrix. Including the adjoint lowering
generator gives a completely positive averaging flow with an explicit
spectral gap. Applied to the original highest cut, this flow produces
a positive, uniformly conditioned probe in time \(O(N^2\log N)\).

This is a one-head theorem in the uniform physical metric. It
does not identify a geometric packet or evaluate a knot invariant.
In particular, it supplies no spectral estimate for a many-head
coproduct system.

## 1. The actual generators and metric

Fix \(N\ge2\), \(d=N-1\), and
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad x=-q^{-1}.
\]
Declare the physical head basis \(w_0,\ldots,w_d\) orthonormal.
Use exactly the balanced complete-root matrices
\[
 \mathcal E w_a=(Q^{-a}-1)w_{a-1},\qquad
 Fw_a=(1-Q^{a+1})w_{a+1},\qquad
 Kw_a=xQ^{-a}w_a.
 \tag{1}
\]
The missing bottom and top arrows are zero.
Here \(\mathcal E\) is the physical lowering operator called \(E\)
in the uniform-physical source and \(\mathcal E\) in the
Azumaya-head calculation. It is not the latter's rescaled
unrestricted generator \(\mathcal E/(q-q^{-1})^2\).
Directly,
\[
 K^*K=I,\qquad K\mathcal EK^{-1}=Q\mathcal E,\qquad
 F=-\mathcal E^*,\qquad
 \|\mathcal E\|_{\rm op},\|F\|_{\rm op}\le2.
 \tag{2}
\]

All matrix norms below are the unnormalized Hilbert--Schmidt norm
\(\|A\|_2^2=\operatorname{Tr}(A^*A)\), unless marked as operator
norms. Put
\[
 c(A)=\frac{\operatorname{Tr}A}{N},\qquad
 D(A)=\frac1N\sum_{j=0}^{N-1}K^jAK^{-j}.
 \tag{3}
\]
The trace in (3) is the ordinary matrix trace.
The matrix \(D(A)\) is precisely the diagonal part of \(A\),
and is its Hilbert--Schmidt orthogonal projection onto diagonal
matrices.

## 2. Coercivity of the actual commutators

**Theorem 1.** For every \(A\in\operatorname{End}(V_N)\),
\[
 \boxed{\quad
 \|A-c(A)I\|_2^2
 \le\frac{3N^2}{8}\|[\mathcal E,A]\|_2^2
      +\frac{N^2}{16}\|[K,A]\|_2^2.
 \quad}
 \tag{4}
\]
There is also the symmetric bound
\[
 \boxed{\quad
 \|A-c(A)I\|_2^2
 \le\frac{N^2}{16}
       \left(3\|[\mathcal E,A]\|_2^2+
             3\|[F,A]\|_2^2+\|[K,A]\|_2^2\right).
 \quad}
 \tag{5}
\]
Both bounds hold at every level, with the original zero arrows.

**Proof.** The eigenspaces of the unitary map \(A\mapsto KAK^{-1}\)
are mutually orthogonal in Hilbert--Schmidt norm. They have eigenvalues
\(Q^m\), \(m\in\mathbb Z/N\); its eigenvalue-one space consists
exactly of diagonal matrices. Every other eigenvalue is at distance
at least \(2\sin(\pi/N)\) from one. Multiplication by \(K^{-1}\)
does not change the norm, so
\[
 \|A-D(A)\|_2^2
 \le\frac{\|[K,A]\|_2^2}{4\sin^2(\pi/N)}
 \le\frac{N^2}{16}\|[K,A]\|_2^2.
 \tag{6}
\]
The final inequality uses \(\sin(\pi/N)\ge2/N\).

Write \(D=D(A)=\operatorname{diag}(d_0,\ldots,d_d)\).
The actual lowering arrows give
\[
 \|[\mathcal E,D]\|_2^2
       =\sum_{j=1}^{d}4\sin^2(\pi j/N)|d_j-d_{j-1}|^2.
 \tag{7}
\]
This is the weighted path energy of the elementary-cap Laplacian.
Its written Hardy estimate, Section 5 of [L], gives
\[
 \sum_{j=0}^d|d_j-c(A)|^2
       \le\frac{3N^2}{8}
             \sum_{j=1}^{d}4\sin^2(\pi j/N)|d_j-d_{j-1}|^2.
 \tag{8}
\]
That estimate is for this actual path, including both endpoints,
and holds also at \(N=2\).

By (2), commutation with \(\mathcal E\) raises the \(K\)-conjugation
grade by one. Consequently
\[
 [\mathcal E,D(A)]
    \quad\hbox{is an orthogonal grade projection of }
             [\mathcal E,A].
 \tag{9}
\]
Thus its norm is at most the full defect norm.
The corresponding statement holds for \(F\), with grade lowered
by one. On a diagonal matrix, the two commutator norms are equal
by (2), or directly by (7).

Finally \(A-D(A)\) and \(D(A)-c(A)I\) are orthogonal.
Adding (6) and (8), and using (9), proves (4).
Alternatively average the equal diagonal estimates obtained from
\(\mathcal E\) and \(F\) before adding (6). This proves (5).
No nonunitary matrix-unit or fusion-frame change occurs.

## 3. A positive averaging flow

For a matrix \(X\), let \(\operatorname{ad}_X(A)=[X,A]\).
Its Hilbert--Schmidt adjoint is
\(\operatorname{ad}_X^*=\operatorname{ad}_{X^*}\).
Define
\[
 \mathscr L=
   \operatorname{ad}_{\mathcal E}^*
                         \operatorname{ad}_{\mathcal E}
  +\operatorname{ad}_{F}^*\operatorname{ad}_{F}
  +\operatorname{ad}_{K}^*\operatorname{ad}_{K}.
 \tag{10}
\]
This is a self-adjoint nonnegative operator on the matrix space.
Its energy is exactly the sum of the three squared Ward defects.
Equation (5) implies
\[
 \ker\mathscr L=\mathbb CI,\qquad
 \mathscr L|_{(\mathbb CI)^\perp}
                      \succeq\frac{16}{3N^2}I.
 \tag{11}
\]
Also \(\|\mathscr L\|_{\rm op}\le36\), since a commutator with
\(X\) has Hilbert--Schmidt operator norm at most \(2\|X\|_{\rm op}\).
The order of the lower gap cannot be improved to a larger order:
for \(A=\operatorname{diag}(j-d/2)_{j=0}^d\),
\[
 \|A\|_2^2=\frac{N(N^2-1)}{12},\quad
 \|[\mathcal E,A]\|_2^2=\|[F,A]\|_2^2=2N,\quad [K,A]=0.
 \tag{12}
\]
Its Rayleigh quotient is \(48/(N^2-1)\).

**Theorem 2.** For \(t\ge0\), the map
\[
                         T_t=e^{-t\mathscr L}
 \tag{13}
\]
is completely positive, unital, trace preserving, and
Hilbert--Schmidt self-adjoint. It satisfies
\[
 \boxed{\quad
 \|T_t(A)-c(A)I\|_2
       \le e^{-16t/(3N^2)}\|A-c(A)I\|_2.
 \quad}
 \tag{14}
\]

**Proof.** Write \(\mathcal E=H+iJ\) and \(K=U+iV\), with
all four displayed parts Hermitian. Since \(K\) is normal,
\([U,V]=0\). Equation (2) gives the exact identity
\[
 \mathscr L
    =2\operatorname{ad}_H^2+2\operatorname{ad}_J^2
                +\operatorname{ad}_U^2+\operatorname{ad}_V^2.
 \tag{15}
\]
For any Hermitian matrix \(B\) and \(s>0\),
\[
 e^{-s\operatorname{ad}_B^2}(A)
  =\frac1{\sqrt{4\pi s}}\int_{\mathbb R}
       e^{-u^2/(4s)}e^{iuB}Ae^{-iuB}\,du.
 \tag{16}
\]
Diagonalizing \(B\) proves (16) by the one-dimensional Gaussian
Fourier integral. Its right side is an average of unitary
conjugations, hence is completely positive, unital and trace
preserving.

Apply (16) separately to the four terms in (15), and take the
finite-dimensional Lie product limit. The product limit follows
by expanding each factor through first order: one step has error
\(O(m^{-2})\), so \(m\) steps converge to the exponential of
the sum. Here \(N\) is fixed for this identity; no uniform
approximation by a finite number of steps is required.
Complete positivity, unitality and trace preservation pass to
the limit. Self-adjointness follows directly from (10), not
from self-adjointness of a noncommuting finite product.
Finally (11) and spectral decomposition prove (14).

## 4. Quantitative observation at the original cut

Let \(P\) be any positive trace-one matrix in this same physical
metric. Define the computable Ward bound
\[
 \Delta(A)^2=\frac{N^2}{16}
       \left(3\|[\mathcal E,A]\|_2^2+
             3\|[F,A]\|_2^2+\|[K,A]\|_2^2\right).
 \tag{17}
\]
By Theorem 1, \(\|A-c(A)I\|_2\le\Delta(A)\). Since
\(\|P\|_2\le\operatorname{Tr}P=1\),
\[
 |\operatorname{Tr}(PA)-c(A)|\le\Delta(A),\qquad
 \|A\|_2^2=N|c(A)|^2+\|A-c(A)I\|_2^2.
 \tag{18}
\]
Thus, with \([u]_+=\max(u,0)\),
\[
 \boxed{\quad
 \left[\frac{\sqrt{[\|A\|_2^2-\Delta(A)^2]_+}}{\sqrt N}
                     -\Delta(A)\right]_+
 \le|\operatorname{Tr}(PA)|
 \le\frac{\|A\|_2}{\sqrt N}+\Delta(A).
 \quad}
 \tag{19}
\]
This uses no lower bound for an unknown overlap or denominator.
For example, put
\[
 \mathfrak w(A)^2=
 \|[\mathcal E,A]\|_2^2+\|[F,A]\|_2^2+\|[K,A]\|_2^2.
\]
If \(A\ne0\), \(0\le\varepsilon\le1/4\), and
\(\mathfrak w(A)\le\varepsilon N^{-3/2}\|A\|_2\), then
\(\Delta(A)\le\varepsilon\|A\|_2/\sqrt N\), and (19) gives
\[
 (1-2\varepsilon)\frac{\|A\|_2}{\sqrt N}
 \le|\operatorname{Tr}(PA)|
 \le(1+\varepsilon)\frac{\|A\|_2}{\sqrt N}.
 \tag{20}
\]
For the lower bound use
\(\sqrt{1-\varepsilon^2/N}\ge1-\varepsilon^2/N
 \ge1-\varepsilon\).
In particular a relative Ward defect \(o(N^{-3/2})\) makes
the ratio in (20) tend to one.

The original highest cut is the rank-one orthogonal projector
\(P_0=|w_0\rangle\langle w_0|\), with the actual tail pivots
and framing factors kept in its one-cut operator.
Consequently (18)--(20) apply to this prescribed observation.

## 5. A canonical softened cut and its source scope

Set
\[
 \rho_t=T_t(P_0),\qquad
 t_N=\frac{3N^2}{16}\log(2N).
 \tag{21}
\]
Theorem 2 gives positivity, trace one, and
\[
 \|\rho_t-I/N\|_2
       \le e^{-16t/(3N^2)}\sqrt{1-1/N}.
 \tag{22}
\]
Since operator norm is at most Hilbert--Schmidt norm, for
every \(t\ge t_N\),
\[
 \boxed{\qquad
 \frac{I}{2N}\preceq\rho_t\preceq\frac{3I}{2N},\qquad
                  \operatorname{cond}_2(\rho_t)\le3.
 \qquad}
 \tag{23}
\]
This is an explicit flow from the actual original probe,
constructed from its actual head generators.

It is particularly concrete on this probe: diagonal matrices stay
diagonal. If \(\Delta_{\mathrm{path},N}\) denotes the weighted path
Laplacian with edge weights \(p_j=4\sin^2(\pi(j+1)/N)\),
\(0\le j<d\), direct multiplication in (10) gives
\[
 \mathscr L(\operatorname{diag}a)
              =2\operatorname{diag}(\Delta_{\mathrm{path},N}a),
 \qquad
 \rho_t=\operatorname{diag}
                   (e^{-2t\Delta_{\mathrm{path},N}}\mathbf e_0).
\]
The matrix \(-2\Delta_{\mathrm{path},N}\) has nonnegative
off-diagonal entries and zero row sums. Its exponential therefore
preserves nonnegative vectors and their total sum: this follows
also by shifting its diagonal to make the entire generator
nonnegative and expanding the exponential series.
Thus the softened cut is the probability distribution of a
specified continuous-time walk on the path, starting at vertex zero.
No cyclic endpoint edge has been introduced.

For the fully assembled unmarked one-cut knot operator
\(A_N=K_N I\), with its recorded external normalization included,
\[
                      \operatorname{Tr}(\rho_t A_N)=K_N
                       \qquad(t\ge0).
 \tag{24}
\]
The scalarity used here is the exact original-source scalarity
recorded in [A, Section 4]. Its qualitative consequence that
any trace-one probe gives the same unmarked knot scalar was
already known. The new estimates are the actual-generator
coercivity, the positive flow and its polynomial mixing time.

For an arbitrary marked matrix, the source is not unchanged.
The exact transported identity is instead
\[
 \operatorname{Tr}(P_0T_t(A))=\operatorname{Tr}(\rho_t A).
 \tag{25}
\]
To check it, \(T_t\) preserves adjoints and is Hilbert--Schmidt
self-adjoint, so it is self-adjoint also for the bilinear
trace pairing. Equation (19) bounds the discrepancy from the
cyclic mean when the Ward defects are controlled.
Replacing the marked source by that mean without this control
is not licensed.

All averaging in (21)--(25) concerns the complete one-head
operator after assembly. It does not replace internal cups,
turns or Casimir derivative channels by scalar quotients.
There is no assertion that this heat flow intertwines every
crossing or that it may be inserted independently on all
internal heads. In particular (11) is not a many-head coproduct
gap.

The full source still needs a geometric norm estimate and
source-faithful control of any proposed geometric approximation.
No such approximation, nonzero geometric period, or
finite-exception volume theorem is supplied here.

## Complete inputs and coverage

The three complete proof inputs were read at these versions.
Theorem 1 uses the actual weighted path estimate of [L];
all new grading, heat-flow and observation calculations are
written above.

| Input | SHA-256 |
|---|---|
| [L: Elementary cap path Laplacian](research_elementary_cap_path_laplacian.md), 355 lines | 0e6ec0f5bfc4fa3e46184c405468144b1c99a41d2dda9fc6a78304e67e679d4f |
| [A: Actual head and original cut](research_actual_head_azumaya_and_cut_descent.md), 327 lines | 1771973ccf96f03e90ec757c9988aa27263a3af02f02e5143a9d9e5445162ffa |
| [Uniform physical source](research_conway_uniform_physical_quartic.md), 477 lines | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |

The complete 494-line original-almost-invariance note was read at
66f4c93efa35425444fbdf90728dcfd254496f3d17f48a7cf6310867fde2cc15,
and the complete 216-line simultaneous-Ward diagnostic at
b97f3f401a53b8ccef359666932b4616c83ac67b7e5ee980f6f9a2c49332b1ad.
They concern different Newton-vector and many-head systems;
their unresolved estimates are not inferred from this one-head result.
No general novelty is claimed for Schur's lemma, Hilbert--Schmidt
orthogonal projection, or completely positive heat semigroups.
The quantitative assertions above concern the displayed original
root head and its prescribed cut.

Only written mathematics and text/hash operations were used.
No mathematical program, numerical experiment, build, git action,
or earlier-final edit was performed.
