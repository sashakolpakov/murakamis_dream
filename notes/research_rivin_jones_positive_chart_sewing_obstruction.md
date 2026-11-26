# Two local positive crossing charts cannot be sewn across a two-crossing twist

Private written deduction, 14 November 2026. No frozen manuscript,
external code, numerical calculation, or test is used here.

The exact Rivin-to-Newton adapter identifies an arbitrary signed block
with its original physical block. It does not supply a new positive
complex contour. In fact the existing exact physical Fourier kernel
already gives nonzero local densities and a positive octahedral chart.
Two source-specific calculations below show why applying that chart
independently at every original crossing cannot prove general short
filling. The obstruction occurs in the actual two-crossing block
\(R_+^2\), before any arbitrary replacement exterior is chosen.

## 1. The actual local positive chart

Use the exact four-function Fourier kernel from
[the balanced crossing theorem](actual_balanced_fourier_crossing_kernel.md),
including its original Cartan scalar, Gaussian, and logarithmic marks.
For its input ports \(z_0,z_1\) and output ports \(z_6,z_7\), the
classical shapes in its signed regulator are
\[
 u=-z_1/z_0,\qquad v=-z_6/z_7,\qquad w=z_7/z_1,
 \qquad D(u)+D(v)+D(w)-D(uvw).
 \tag{1}
\]
The positive chart uses the four positively oriented shapes
\(u,v,w,(uvw)^{-1}\). On its unit-angle locus their angles lie
in \((0,\pi)\) and sum to \(2\pi\). Its kernel has the nonzero
source-normalized density proved in the cited note.

Now compose two positive crossings on the same adjacent heads, using
the coherently propagated Fourier frames. Those frames make the
interior adapters exactly the identity, as proved in
[the propagated-frame theorem](propagated_balanced_frames_and_boundary_source.md).
The first crossing's output ports are literally the second crossing's
input ports:
\[
 z'_0=z_6,\qquad z'_1=z_7.
\]
Consequently their shapes obey the exact algebraic relation
\[
                         u'=\frac1v.
 \tag{2}
\]

**Lemma 1.** The product of these two local positive octahedral
charts has empty intersection with the actual interior sewing equations.

*Proof.* For every nonreal \(v\),
\[
                   \operatorname{Im}(1/v)
                    =-\frac{\operatorname{Im}v}{|v|^2}.
\]
Thus \(\operatorname{Im}v>0\) and \(\operatorname{Im}u'>0\)
cannot both hold under (2). \(\square\)

This concerns the original signed shapes in (1). Cyclic positive quad
rotations do not repair it: the maps \(z\), \(1/(1-z)\), and
\(1-1/z\) each preserve the sign of the imaginary part. Declaring
the reciprocal tetrahedron positive would change its orientation and
its signed action unless an additional source identity is supplied.

At finite level the full functions have their recorded \(q\)-shifts.
These do not permit both crossings to lie in fixed compact subsets of
their strict positive classical charts as \(N\to\infty\). The
limiting relation remains (2). Any apparent repair confined to angles
of order \(1/N\) approaches a degenerate boundary rather than a
strict positive geometric chart.

The lemma is independent of the external boundary parameters. In
particular, requiring those parameters to arise from a positive
hyperbolic geometric representation does not make these two original
local charts compatible. It does not exclude a positive triangulation
of the component after fusing or changing its internal decomposition.
Such a change needs its own exact source comparison.

## 2. The same two-crossing block has a nontrivial sewn deck character

There is a separate exact obstruction to treating the finite Fourier
polynomial as the raw four-function continuation on a whole complex
torus. Put \(s=(-1)^{N+1}\). Use logarithmic ports
\((a,b;c,d)\) for the first crossing and \((c,d;e,f)\) for the
second. Their central coordinates are
\[
 A=e^{Na},\ B=e^{Nb},\ C=e^{Nc},\ D=e^{Nd},\ E=e^{Ne},\ F=e^{Nf}.
\]
Write \(M_N(a,b,c,d)\) for the specific raw full-function continuation
fixed in [the deck-character calculation](balanced_crossing_deck_characters.md),
and set
\[
              \mathscr M_N=M_N(a,b,c,d)M_N(c,d,e,f).
 \tag{3}
\]
No contour transformation is implicit in (3).

The exact local full-turn characters needed here are
\[
 \mu_a=\frac{sC(A-sB)}{B(A-C)},\quad
 \mu_b=\frac{s(D-B)}{A-sB},\quad
 \mu_c=\frac{s(A-C)}{D-sC},\quad
 \mu_d=\frac{sB(D-sC)}{C(D-B)}.
 \tag{4}
\]
The sewn characters in the two internal variables are their actual
products. Cancellation of the displayed factors gives
\[
 \nu_c=-\frac{sE(A-C)}{D(C-E)},\qquad
 \nu_d=-\frac{sB(F-D)}{C(D-B)}.
 \tag{5}
\]
These identities hold wherever the written ratios are regular and
extend meromorphically across removable factors.

The propagated two-crossing central frames have
\[
                    C=sB,\quad D=sA,\quad E=A,\quad F=B.
 \tag{6}
\]
Keep the external central values \(E=A,F=B\), but allow the internal
ports to move. Then (5) simplifies to
\[
                         \nu_c=\frac{sA}{D},\qquad
                         \nu_d=\frac{sB}{C}.
 \tag{7}
\]
Thus identity interior frame adapters do not make this raw continued
product periodic away from the original balanced sampling multisection.

## 3. A microscopic movement already forces a same-order correction

Choose regular nonzero \(A,B\) with \(B\ne sA\), and fix a
nonzero constant \(\lambda\ne1\) sufficiently close to one to avoid
the other displayed divisors. Starting at (6), move only
\[
                    c\longmapsto c+\frac{\log\lambda}{N}.
 \tag{8}
\]
This changes \(C\) to \(\lambda sB\), while \(D=sA\) remains.
It is precisely the microscopic scale of a change between bounded
Fourier-radius frames. Equations (7) now give
\[
                          \nu_c=1,\qquad \nu_d=\lambda^{-1}.
 \tag{9}
\]
The defect is independent of \(N\), including its parity.

Let \(\mathscr P_N\) be the product of the actual two finite Fourier
Laurent-polynomial crossing interpolants, with the same shared ports.
It is fixed by the original finite matrices. In particular it is
\(2\pi i\)-periodic in \(d\). It agrees with (3) on the original
sampling grids, but no off-grid equality is assumed. Let \(p\) be
the point after (8), and let \(p^+\) be the same point with
\(d\) replaced by \(d+2\pi i\).

**Lemma 2.** Wherever the raw product is regular,
\[
 \max\bigl\{
 |\mathscr P_N(p)-\mathscr M_N(p)|,
 |\mathscr P_N(p^+)-\mathscr M_N(p^+)|
 \bigr\}
 \ \ge\ \frac{|1-\lambda^{-1}|}{2}|\mathscr M_N(p)|.
 \tag{10}
\]

*Proof.* Periodicity gives \(\mathscr P_N(p^+)=\mathscr P_N(p)\),
whereas the exact character (9) gives
\(\mathscr M_N(p^+)=\lambda^{-1}\mathscr M_N(p)\).
Subtract the two errors and apply the triangle inequality. \(\square\)

In particular there is no relative \(o(1)\) identification of the
actual finite polynomial with the raw full-function continuation on
a domain containing both lips, even after a displacement of order
\(1/N\). If the raw product has a given exponential rate along the
chosen points, at least one correction in (10) has that rate or larger.
This is a statement about density values. It does not give a lower
bound for an integrated seam period, whose terms may themselves cancel.

The exact one-port and paired-port interpolation theorems in
[the physical port-polynomial note](actual_fourier_port_polynomials_and_profiles.md)
remain valid. Their fixed opposite grids and retained central factors
are exactly what distinguish them from the simultaneous raw
continuation ruled out by (10).

## 4. Consequence for the short-filling route

These are two concrete gaps in a proposed universal argument from
nonzero local Fourier kernels to a nonzero geometric coefficient.
The original two-crossing twist cannot be placed in the product of
the known strict positive local charts. Its raw continued Fourier
product also needs a correction of nonnegligible relative size when
microscopic frame movements are made across a full logarithmic cycle.

Thus a general proof must do more than complete each crossing into
its known nonzero full-function block, reflect the negative crossings,
and apply positive-volume concavity. It must transform or fuse the
actual block before imposing the positive chart, and preserve the
finite boundary and seam source in that transformation. Neither lemma
rules out such a transformation, or the original volume conjecture.
They identify precisely why the new local matrix adapter alone does
not provide it.
